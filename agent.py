import os
from dotenv import load_dotenv
#ds的接口和openai一样，用工具去连ds
from langchain_openai import ChatOpenAI
#把python代码变成AI能看懂的tool
from langchain_core.tools import tool
#负责LLM和tools的拼接
from langchain_classic.agents import create_tool_calling_agent, AgentExecutor
#给AI写规章制度
from langchain_core.prompts import ChatPromptTemplate

# 1. 加载钥匙
load_dotenv()

# 2. 配置大模型
llm = ChatOpenAI(
    model="deepseek-chat",
    base_url="https://api.deepseek.com/v1",
    api_key=os.getenv("DEEPSEEK_API_KEY")
)

# 3. 制作工具（@tool 是核心！）
@tool
def add(a: float, b: float) -> float:
    """计算两个数相加"""
    return a + b

@tool
def multiply(a: float, b: float) -> float:
    """计算两个数相乘"""
    return a * b

tools = [add, multiply]

# 4. 给 Agent 立下规矩（Prompt）
prompt = ChatPromptTemplate.from_messages([
    ("system", "你是一个会用工具的助手，遇到数学题请务必调用工具计算。"),
    ("human", "{input}"),
    ("placeholder", "{agent_scratchpad}"), # 留给 Agent 思考的空白区
])

# 5. 组装大师把大脑、工具和规矩组装成 Agent
agent = create_tool_calling_agent(llm, tools, prompt)

# 6. 创建执行器（verbose=True 打开“上帝视角”，看它怎么思考，verbose是冗长的解题过程）
executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# 7. 提问！
print("\n==== 开始提问 ====")
executor.invoke({"input": "3.5 加 4.8 等于多少？然后再把这个结果乘 6 呢？"})