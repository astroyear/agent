from langchain_core.output_parsers import StrOutputParser, JsonOutputParser
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.prompts import PromptTemplate

str_parser = StrOutputParser()
json_parser = JsonOutputParser()

model = ChatTongyi(model="qwen3-max")
first_prompt = PromptTemplate.from_template(
    "我邻居姓{lastname}，刚生了{gender}，请帮忙起名字，仅回复一个名字，"
    "要求封装为json格式返回给我，key为name，value是你起的名字"
)
second_prompt = PromptTemplate.from_template(
    "姓名{name}，请帮我解析含义"
)

chain = first_prompt | model | json_parser | second_prompt | model | str_parser

# res = chain.invoke({"lastname":"张","gender":"女儿"})
# print(res)
# print(type(res))

for chunk in chain.stream({"lastname":"张","gender":"女儿"}):
    print(chunk,end="",flush=True)