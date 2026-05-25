from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.messages import HumanMessage,AIMessage,SystemMessage

model = ChatTongyi(model="qwen3-max")

messages = [
    ("system","你是只猫"),
    ("human","你是猫吗"),
    ("ai","不是"),
    ("human","?")
]

res = model.stream(input=messages)

for chunk in res:
    print(chunk.content,end="",flush=True)