from langchain_community.llms.tongyi import Tongyi

model = Tongyi(model="qwen-max")

res = model.stream(input="你知道shanoa是谁吗？")

for chunk in res:
    print(chunk,end="",flush=True)