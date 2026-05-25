from openai import OpenAI

client = OpenAI(
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)
response = client.chat.completions.create(
    model="qwen-max",
    messages=[
        {"role":"system","content":"你是一个编程专家"},
        {"role":"assistant","content":"好"},
        {"role":"user","content":"写一下for1-10数字"}
    ],
    stream=True
)
# print(response.choices[0].message.content)

for chunk in response:
    print(chunk.choices[0].delta.content,end="",flush=True)
