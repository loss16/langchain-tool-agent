import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# 读取 .env 里的 Key
load_dotenv()

# 配置大模型
llm = ChatOpenAI(
    model="deepseek-chat",
    base_url="https://api.deepseek.com/v1",
    api_key=os.getenv("DEEPSEEK_API_KEY"),
)

# 问一个简单的问题
response = llm.invoke("用一句话解释什么是 AI Agent")
print("\n==== 模型回复 ====\n", response.content)