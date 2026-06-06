from fastapi import FastAPI
from pydantic import BaseModel

from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.llms import Ollama

app = FastAPI(title="RAG Service")

embeddings = OllamaEmbeddings(model="nomic-embed-text")

db = Chroma(
    persist_directory="chroma_db",
    embedding_function=embeddings
)

retriever = db.as_retriever(search_kwargs={"k": 3})

llm = Ollama(model="llama3")

class QueryRequest(BaseModel):
    question: str

@app.get("/")
def home():
    return {"message": "RAG Service Running"}

@app.post("/ask")
def ask_question(request: QueryRequest):

    docs = retriever.invoke(request.question)

    context = "\n".join([doc.page_content for doc in docs])

    prompt = f"""
Answer using only the provided context.

Context:
{context}

Question:
{request.question}
"""

    answer = llm.invoke(prompt)

    return {
        "question": request.question,
        "answer": answer
    }