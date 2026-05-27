from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_community.chat_models.tongyi import ChatTongyi

chat_prompt_template = ChatPromptTemplate.from_messages(
  [
    ("system","你是个诗人"),
    MessagesPlaceholder("history"),
    ("human","继续来一首唐诗")
  ]
)

history_data = [
  ("human","写首诗出来"),
  ("ai","床前明月光")
]

model = ChatTongyi(model="qwen3-max")

chain = chat_prompt_template | model
# res = chain.invoke({"history":history_data})
# print(res.content)

for chunk in chain.stream({"history":history_data}):
  print(chunk.content, end="", flush=True)