"""
    这是用langchain框架 调用了
"""



# main.py
from dotenv import load_dotenv
import os

def print_hi():
    import getpass
    import os
    load_dotenv()
    print(os.environ["GROQ_API_KEY"])
    from langchain_groq import ChatGroq

    llm = ChatGroq(
        model="llama-3.1-8b-instant",
        temperature=0,
        max_tokens=None,
        timeout=None,
        max_retries=2,
        # other params...
    )
    messages = [
        (
            "system",
            "You are a helpful assistant that translates English to French. Translate the user sentence.",
        ),
        ("human", "I love programming."),
    ]
    ai_msg = llm.invoke(messages)
    print(ai_msg.content)

if __name__ == "__main__":
    print_hi()
