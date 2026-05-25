from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.messages import HumanMessage,AIMessage,SystemMessage

model = ChatTongyi(model="qwen3-max")

messages = [
    SystemMessage(content="你是一只猫"),
    HumanMessage(content="写一首唐诗"),
    AIMessage(content="喵"),
    HumanMessage(content="？")
]

res = model.stream(input=messages)

for chunk in res:
    print(chunk.content,end="",flush=True)