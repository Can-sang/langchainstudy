# 📚 项目介绍：LangChain + Groq 小项目实战

本项目使用 [LangChain](https://python.langchain.com/) 框架结合 [Groq API](https://groq.com/) 搭建一个基础的 **LLM 应用**，包括以下示例内容：

- **普通对话**
- **链式调用（Chain）**
- **流式输出（Stream）**
- **文档管理与向量库（RAG 基础）**

---

## 🏗️ 技术栈

| 技术            | 用途               |
| ------------- | ---------------- |
| `LangChain`   | 框架，负责对接模型、RAG 等  |
| `Groq API`    | LLM（大模型）提供者      |
| `FAISS`       | 本地向量存储           |
| `HuggingFace` | 文本转向量（Embedding） |

---

## 🚀 快速上手

### 1️⃣ 安装依赖

```bash
pip install -U langchain-core langchain-community langchain-groq langchain-openai faiss-cpu huggingface-hub
```

### 2️⃣ 配置环境变量

在根目录下新建 `.env` 文件，内容示例：

```dotenv
GROQ_API_KEY=你的GROQ密钥
HUGGINGFACEHUB_API_TOKEN=你的HuggingFace密钥
LANGSMITH_API_KEY=你的LangSmith密钥（可选，用于调试监控）
```

---

### 3️⃣ 启动项目

运行你的主程序，例如：

```bash
python main.py
```

---

## 💡 示例效果

### ✅ 普通对话

```python
messages = [("system", "You are helpful."), ("human", "How can I make money with computers?")]
stream = llm.stream(messages)
for chunk in stream:
    print(chunk.text(), end="")
```

---

### ✅ 链式调用 Chain

```python
prompt = ChatPromptTemplate.from_messages([
    ("system", "You translate {input_language} to {output_language}.")
    ("human", "{input}")
])
chain = prompt | llm
response = chain.invoke({
    "input_language": "English",
    "output_language": "German",
    "input": "I love programming."
})
print(response.content)
```

---

### ✅ 文档管理 & 向量库（RAG 简易示例）

```python
from langchain_core.documents import Document
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

docs = [Document(page_content="Air Jordan 1 是 1985 年推出的篮球鞋。")]
vectorstore = FAISS.from_documents(docs, HuggingFaceEmbeddings(model_name="BAAI/bge-small-en-v1.5"))
```

---

## 📎 学习资料

本项目学习资料、灵感来源于： 👉 [https://github.com/gkamradt/langchain-tutorials](https://github.com/gkamradt/langchain-tutorials?tab=readme-ov-file)

---

## 🙌 致谢

感谢以上开源资料，让初学者也能快速入门 LLM 技术与 LangChain 框架。

