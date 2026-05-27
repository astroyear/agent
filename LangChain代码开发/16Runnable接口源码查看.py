from langchain_core.prompts import PromptTemplate
from langchain_community.llms.tongyi import Tongyi

prompt = PromptTemplate.from_template("你是一个AI助手")
model = Tongyi(model="qwen3-max")

chain = prompt | model | prompt | model
print(type(chain))

#runnableSequence是runnable接口的子类，底层是通过Runnable对魔术方法__or__的重写来返回runnableSequence这个类
# 那对于chain，其类型就是RunnableSequence，不管多少个组件加进来，永远只有这一个对象，
# 最后通过调用该对象.invoke，就是按顺序调用那些组件的invoke，前一个组件的输出作为下一个组件的输入