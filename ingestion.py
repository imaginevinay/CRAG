from dotenv import load_dotenv
load_dotenv()
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import WebBaseLoader
from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings



urls = [
    "https://lilianweng.github.io/posts/2023-06-23-agent/",
    "https://lilianweng.github.io/posts/2023-03-15-prompt-engineering/",
    "https://lilianweng.github.io/posts/2023-10-25-adv-attack-llm/",
]

# 1. load the urls into langchain docs
docs = [WebBaseLoader(url).load() for url in urls]

# 2. flatten this list
docs_list = [item for sublist in docs for item in sublist]

# 3. split into chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=100)
doc_splits = text_splitter.split_documents(docs_list)

# 4. index these chunks into chromaDB
vectorStore = Chroma.from_documents(
    documents=doc_splits,
    collection_name="rag-chroma",
    embedding=OllamaEmbeddings(model="qwen2:1.5b"),
    persist_directory="./.chroma"
)

# 5. retirever from chroma DB
retreiver = Chroma(
    collection_name="rag-chroma"   ,
    persist_directory="./.chroma",
    embedding_function=OllamaEmbeddings(model="qwen2:1.5b")
).as_retriever()