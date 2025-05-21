from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.llms import LlamaCpp
from langchain.chains import RetrievalQA
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter

loader = TextLoader("data/README-test.md")
# loader = TextLoader("data/README-http-server.md")
docs = loader.load()
split_docs = CharacterTextSplitter(chunk_size=500, chunk_overlap=50).split_documents(docs)

embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
db = FAISS.from_documents(split_docs, embedding_model)
db.save_local("embeddings")

db = FAISS.load_local("embeddings", embedding_model, allow_dangerous_deserialization=True)

llm = LlamaCpp(model_path="models/ggml-tinyllama-q4_0.bin", temperature=0.5, max_tokens=256, verbose=False, n_ctx=2048)

qa = RetrievalQA.from_chain_type(llm=llm, retriever=db.as_retriever())
