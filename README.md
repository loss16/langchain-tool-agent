# 基于 LangChain 与 DeepSeek 的工具调用（Tool Calling）Agent

## 项目简介
本项目是一个具备工具调用能力的 AI Agent 原型。通过引入 Tool Calling 机制，让大模型能够自主思考，并在遇到数学计算任务时，动态调用本地 Python 函数，突破了 LLM 原生计算能力弱和易产生幻觉的瓶颈。

## 技术栈
- 框架：LangChain (langchain-classic)
- 大模型：DeepSeek API
- 核心组件：AgentExecutor, Tool, Prompt Template

## 核心亮点
1. 完整跑通 LLM -> 工具调用 -> 结果反馈 -> 再次思考的 Agent 闭环链路。
2. 掌握 ReAct 模式，通过 verbose 模式清晰观察 Agent 的 Thought -> Action -> Observation 过程。
3. 成功解决 LangChain 新老版本 API 弃用冲突（通过引入 langchain-classic 兼容包）。

## 运行方式
1. 安装依赖：`pip install langchain langchain-openai langchain-classic python-dotenv`
2. 在根目录配置 `.env` 文件（包含 `DEEPSEEK_API_KEY`）。
3. 运行 `agent.py` 即可。