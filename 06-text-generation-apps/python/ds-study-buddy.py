from openai import OpenAI
import os
from dotenv import load_dotenv

# 从 .env 文件加载环境变量
load_dotenv()

# 配置 Azure OpenAI 服务客户端
client = OpenAI()
deployment = "deepseek-chat"

# 添加你的补全代码
question = input("向你的学习伙伴提出关于 Python 语言的问题: ")
prompt = f"""
你是 Python 语言的专家。

当被问到某些问题时，你需要按照以下格式提供回答。

- 概念
- 展示概念实现的示例代码
- 对示例的解释以及如何实现概念，以便用户更好地理解。

回答问题: {question}
"""
messages = [{"role": "user", "content": prompt}]
# 进行补全
completion = client.chat.completions.create(model=deployment, messages=messages)

# 打印响应
print(completion.choices[0].message.content)

#  非常不开心 _____.

# 很久很久以前，有一条非常不开心的人鱼。
