from langchain_core.output_parsers import StrOutputParser
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.prompts import PromptTemplate

parser = StrOutputParser()
model = ChatTongyi(model="qwen3-max")
prompt = PromptTemplate.from_template("我的邻居姓:{lastname}，帮他给孩子起个名")

chain = prompt | model | parser | model | parser

res = chain.invoke({"lastname":"韩"})
print(res.content)