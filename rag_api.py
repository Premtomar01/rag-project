from fastapi import FastAPI
from pydantic import BaseModel

from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.llms import Ollama
from hybrid_search import hybrid_search

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

@app.post("/ask")

def ask_question(request: QueryRequest):

    result = hybrid_search(request.question)

    if result["source"] == "database":

        emp = result["data"]

        context = f"""

Employee Information

ID: {emp[0]}

Name: {emp[1]}

Department: {emp[2]}

Leave Balance: {emp[3]}

Salary: {emp[4]}

"""

    else:

        docs = retriever.invoke(request.question)

        context = "\n".join(

        [doc.page_content for doc in docs]

        )

    prompt = f"""

Answer using the information below.

Context:

{context}

Question:

{request.question}

"""

    answer = llm.invoke(prompt)

    return {

    "source": result["source"],

    "answer": answer

    }