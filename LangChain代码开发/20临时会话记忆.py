from langchain_core.output_parsers import StrOutputParser
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.prompts import PromptTemplate, MessagesPlaceholder, ChatPromptTemplate
from langchain_core.runnables import RunnableLambda
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.chat_history import InMemoryChatMessageHistory

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

store = {}          #key就是sessionId，value就是InMemoryChatMessageHistroy的类对象
def get_history(session_id):
    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory()
    return store[session_id]


#创建新链，对原有链增强，自动附加历史信息
conversation_chain = RunnableWithMessageHistory(
    base_chain,         #要被增强的原链
    get_history,        #通过会话id获得InMemoryChatMessageHistory类对象
    input_messages_key="input",
    history_messages_key="chat_history"
)

if __name__ == '__main__':
    session_config = {
        "configurable": {
            "session_id": "user_001"
        }
    }

    res = conversation_chain.invoke({"input":"小明有两只猫"},session_config)
    print("第一次执行：", res)

    res = conversation_chain.invoke({"input": "小明有一只狗"}, session_config)
    print("第二次执行：", res)

    res = conversation_chain.invoke({"input": "总共多少只动物"}, session_config)
    print("第三次执行：", res)