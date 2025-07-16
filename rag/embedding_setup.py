# embedding_setup.py
from dotenv import load_dotenv
import os
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.schema import Document

def build_vectorstore(doc_texts: list[str]) -> FAISS:
    load_dotenv()
    hf_token = os.getenv("HUGGINGFACEHUB_API_TOKEN")

    # 1. 初始化 HuggingFace 嵌入模型
    embedder = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2",
        huggingfacehub_api_token=hf_token
    )

    # 2. 将文本列表封装为 Document（可加入 metadata）
    docs = [Document(page_content=text) for text in doc_texts]

    # 3. 用 FAISS 构建向量索引
    vectorstore = FAISS.from_documents(docs, embedder)
    return vectorstore
