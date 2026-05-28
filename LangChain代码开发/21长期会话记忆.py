import os, json
from msilib.schema import Property
from typing import Sequence
from langchain_core.messages import message_to_dict, messages_from_dict, BaseMessage  # 单消息对象转化为dict，
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.output_parsers import StrOutputParser
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.prompts import PromptTemplate, MessagesPlaceholder, ChatPromptTemplate
from langchain_core.runnables import RunnableLambda
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.chat_history import InMemoryChatMessageHistory



class FileChatMessageHistory(BaseChatMessageHistory):
    def __init__(self, session_id, storage_path):
        self.session_id = session_id
        self.storage_path = storage_path

        self.file_path = os.path.join(self.storage_path,self.session_id)
        os.makedirs(os.path.dirname(self.file_path),exist_ok=True)

    def add_messages(self, messages: Sequence[BaseMessage]) -> None:
        all_messages = list(self.messages)
        all_messages.extend(messages)

        #直接将类对象写入文件是一堆二进制，看不懂，所以要序列化转成字典再json写入。
        new_messages = []
        for message in all_messages:
            d = message_to_dict(message)
            new_messages.append(d)

        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump(new_messages,f)

    @property
    def messages(self) -> list[BaseMessage]:
        try:
            with open(self.file_path, "r", encoding="utf-8") as f:
                messages_data = json.load(f)
                return messages_from_dict(messages_data)
        except FileNotFoundError:
            return[]

    def clear(self) -> None:
        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump([],f)


model = ChatTongyi(model="qwen3-max")
# prompt = PromptTemplate.from_template(
#     "你需要根据会话历史回应用户问题。对话历史：{chat_history}，用户提问：{input}，请回答"
# )

prompt = ChatPromptTemplate.from_messages(
    [
        ("system","你需要根据会话历史回应用户问题。对话历史："),
        MessagesPlaceholder("chat_history"),
        ("human","请回答问题：{input}")
    ]
)

str_parser = StrOutputParser()

def print_prompt(full_prompt):
    print("="*20,full_prompt.to_string(),"="*20)
    return full_prompt

base_chain = prompt | print_prompt | model | str_parser

def get_history(session_id):
    return FileChatMessageHistory(session_id, "./chat_history")


#创建新链，对原有链增强，自动附加历史信息
conversation_chain = RunnableWithMessageHistory(
    base_chain,         #要被增强的原链
    get_history,        #通过会话id获得类对象
    input_messages_key="input",
    history_messages_key="chat_history"
)

if __name__ == '__main__':
    session_config = {
        "configurable": {
            "session_id": "user_001"
        }
    }

    # res = conversation_chain.invoke({"input":"小明有两只猫"},session_config)
    # print("第一次执行：", res)
    #
    # res = conversation_chain.invoke({"input": "小明有一只狗"}, session_config)
    # print("第二次执行：", res)

    res = conversation_chain.invoke({"input": "总共多少只动物"}, session_config)
    print("第三次执行：", res)