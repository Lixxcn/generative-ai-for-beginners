from openai import OpenAI
from dotenv import load_dotenv

# 从 .env 文件加载环境变量
load_dotenv()

# 配置 Azure OpenAI 服务客户端
client = OpenAI()
deployment = "deepseek-chat"

no_recipes = input("食谱数量 (例如, 5): ")

ingredients = input("食材列表 (例如, 鸡肉、土豆和胡萝卜): ")

filter = input("过滤条件 (例如, 素食、纯素或无麸质): ")

# 将食谱数量和食材插入到提示词中
prompt = f"请给我 {no_recipes} 个包含以下食材的菜谱: {ingredients}. 每个菜谱列出所有使用的食材, 不要 {filter}: "
messages = [{"role": "user", "content": prompt}]

completion = client.chat.completions.create(
    model=deployment, messages=messages, max_tokens=600, temperature=0.1
)


# 打印响应
print("菜谱:")
print(completion.choices[0].message.content)

old_prompt_result = completion.choices[0].message.content
prompt_shopping = "生成一个购物清单, 请不要包含我家里已经有的食材: "

new_prompt = (
    f"根据家里的食材 {ingredients} 和生成的菜谱: {old_prompt_result}, {prompt_shopping}"
)
messages = [{"role": "user", "content": new_prompt}]
completion = client.chat.completions.create(
    model=deployment, messages=messages, max_tokens=600, temperature=0
)

# 打印响应
print("\n=====购物清单 ======= \n")
print(completion.choices[0].message.content)
