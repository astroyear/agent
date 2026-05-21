from openai import OpenAI

client = OpenAI(
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)
response = client.chat.completions.create(
    model="qwen-max",
    messages=[
        {"role":"system","content":"你是一个AI助理，回答很简洁"},
        {"role":"user","content":"小明有2条狗"},
        {"role":"assistant","content":"好"},
        {"role":"user","content":"小红有3只猫"},
        {"role":"assistant","content":"好"},
        {"role":"user","content":"有多少只动物？"}
    ],
    stream=True
)
# print(response.choices[0].message.content)

for chunk in response:
    print(chunk.choices[0].delta.content,end="",flush=True)