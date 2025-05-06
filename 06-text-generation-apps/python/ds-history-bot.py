from openai import OpenAI
import os
from dotenv import load_dotenv

# 从 .env 文件加载环境变量
load_dotenv()

# 配置 Azure OpenAI 服务客户端
client = OpenAI()
deployment = "deepseek-chat"

# 添加你的补全代码
persona = input("告诉我你想扮演的历史人物: ")
question = input("提出你关于这个历史人物的问题: ")
prompt = f"""
你将扮演历史人物 {persona}。

当被问到某些问题时，你需要记住时间线和事件的事实，并且只回答准确的答案。不要自己创造内容。如果你不知道，就说你不记得了。

回答问题: {question}
"""
messages = [{"role": "user", "content": prompt}]
# 进行补全
completion = client.chat.completions.create(
    model=deployment, messages=messages, temperature=0
)

# 打印响应
print(completion.choices[0].message.content)

#  非常不开心 _____.

# 很久很久以前，有一条非常不开心的人鱼。
