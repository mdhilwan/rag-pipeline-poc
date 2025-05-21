from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.llms import LlamaCpp
from langchain.chains import RetrievalQA
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
import os

# Load & split your API docs
loader = TextLoader("data/api_docs.txt")
docs = loader.load()
text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
split_docs = text_splitter.split_documents(docs)

# Embed documents
embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
db = FAISS.from_documents(split_docs, embedding_model)

# Save vector store (once)
db.save_local("embeddings")

# Load vector store & run querys
db = FAISS.load_local("embeddings", embedding_model, allow_dangerous_deserialization=True)

llm = LlamaCpp(
    model_path="models/ggml-tinyllama-q4_0.bin",  # use a quantized model here
    temperature=0.5,
    max_tokens=256,
    verbose=True,
)

qa = RetrievalQA.from_chain_type(llm=llm, retriever=db.as_retriever())
query = input("Ask something: ")
result = qa.invoke(query)
print("\nAnswer:", result)
