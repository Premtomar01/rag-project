import streamlit as st

from langchain_community.llms import Ollama
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OllamaEmbeddings
from langchain_classic.chains import RetrievalQA

st.title("RAG Chatbot")

embeddings = OllamaEmbeddings(
    model="nomic-embed-text"
)

db = Chroma(
    persist_directory="chroma_db",
    embedding_function=embeddings
)

retriever = db.as_retriever()

llm = Ollama(model="llama3")

qa = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever
)

query = st.text_input("Ask Question")

if query:
    answer = qa.run(query)
    st.write(answer)