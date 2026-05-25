from langchain_core.prompts import ChatPromptTemplate, MessagePlaceholder
from langchain_community.char_models.tongyi import ChatTongyi

chat_prompt_template = ChatPromptTemplate.from_message(
  [
    ("system","你是个诗人")
    MessagePlaceholder("history")
    ("human","继续来一首唐诗")
  ]
)

history_data = [
  ("human","写首诗出来")
  ("ai","床前明月光")
]

prompt_text = chat_prompt_template.invoke({"history":"history_data"}).to_string()

model = ChatTongyi(model="qwen3-max")
res = model.invoke(prompt_text)
print(res.content,type(res))
