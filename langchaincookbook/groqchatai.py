"""
    这是用langchain框架 调用了
"""



# main.py
from dotenv import load_dotenv
import os

def chatai():
    import getpass
    import os
    load_dotenv()
    # print(os.environ["GROQ_API_KEY"])
    from langchain_groq import ChatGroq
    # 实例化 模型的实例化
    llm = ChatGroq(
        model="llama-3.1-8b-instant",  #deepseek-r1-distill-llama-70b      llama-3.1-8b-instant  qwen/qwen3-32b
        temperature=0,
        max_tokens=None,
        timeout=None,
        max_retries=2,
        # other params...
    )

    """
        1.    
        普通调用LLM
        将消息体写死
    """
    messages = [
        (
            "system",
            "You are a nice AI bot that helps a user figure out what to eat in one short sentence",
        ),
        ("human", "I like tomatoes, what should I eat?"),
    ]

    ai_msg = llm.invoke(messages)   #将消息与LLM模型交互
    # print(ai_msg.content)

    """
        2.
        链式调用LLM
        模板定义对话结构
    """
    from langchain_core.prompts import ChatPromptTemplate

    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "You are a helpful assistant that translates {input_language} to {output_language}.",
            ),
            ("human", "{input}"),
        ]
    )

    chain = prompt | llm  #1️⃣ 用输入变量，生成完整对话 prompt   #2️⃣ 把 prompt 发给 LLM，获取回答
    ai_msg = chain.invoke(
        {
            "input_language": "English",
            "output_language": "German",
            "input": "I love programming.",
        }
    )
    """
        3.
        | 用途       | 内容                                                    |
        | -------- | ----------------------------------------------------- |
        | **输出内容** | `content`，直接拿来展示 / 使用                                 |
        | **推理过程** | `additional_kwargs['reasoning_content']`（可选）          |
        | **消耗情况** | `response_metadata['token_usage']`，帮你看消耗多少 Token / 速度 |
        | **模型信息** | `model_name`，确认是哪个 LLM                                |
    """
    # print(ai_msg.content)
    """
        4.
        流式输出streaming
    """
    # 1. 发起流式请求
    stream = llm.stream([
        ("system","..."),
        ("human", "I want to know how I can make money by studying computers, and make money with high cost performance")
    ])

    # 2. 实时打印
    for chunk in stream:
        print(chunk.text(), end="")

    # 3. 或者拼成完整结果供后续使用
    stream = llm.stream(messages)
    full = next(stream)
    for chunk in stream:
        full += chunk
    print("\n完整翻译：", full.content)


if __name__ == "__main__":
    chatai()
