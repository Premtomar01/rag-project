from fastapi import FastAPI
from pydantic import BaseModel

from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.llms import Ollama

from hybrid_search import hybrid_search

app = FastAPI(title="Hybrid RAG Service")


# -----------------------------
# Embeddings
# -----------------------------

embeddings = OllamaEmbeddings(model="nomic-embed-text")


# -----------------------------
# Vector Database
# -----------------------------

db = Chroma(
    persist_directory="chroma_db",
    embedding_function=embeddings
)

retriever = db.as_retriever(search_kwargs={"k": 4})


# -----------------------------
# LLM
# -----------------------------

llm = Ollama(model="llama3")


# -----------------------------
# Request Model
# -----------------------------

class QueryRequest(BaseModel):
    question: str


# -----------------------------
# API
# -----------------------------

@app.post("/ask")
def ask_question(request: QueryRequest):

    question = request.question

    result = hybrid_search(question)

    route = result["route"]

    context = ""

    sources = []

    # -----------------------------
    # Greeting
    # -----------------------------

    if route == "greeting":

        return {
            "source": "Greeting",
            "answer": "Hello! How can I help you regarding company policies or employee information?"
        }

    # -----------------------------
    # Out of Scope
    # -----------------------------

    if route == "out_of_scope":

        return {
            "source": "Out of Scope",
            "answer": "Sorry, I can answer only questions related to Company Policies and Employee Database."
        }

    # -----------------------------
    # Database Context
    # -----------------------------

    if result["database"]:

        emp = result["database"]

        context += f"""
Employee Information

ID : {emp['id']}
Name : {emp['name']}
Department : {emp['department']}
Leave Balance : {emp['leave_balance']}
Salary : {emp['salary']}
"""

        sources.append("Employee Database")

    # -----------------------------
    # PDF Context
    # -----------------------------

    if result["documents"]:

        docs = retriever.invoke(question)

        pdf_context = "\n\n".join(
            [doc.page_content for doc in docs]
        )

        context += "\n\nCompany Policy Information\n\n"

        context += pdf_context

        sources.append("Company Documents")

    # -----------------------------
    # Prompt
    # -----------------------------

    prompt = f"""
You are an AI Assistant for Cortex Solutions.

Rules:

1. Answer ONLY from the provided context.

2. If information is missing say:
"The provided documents do not contain sufficient information."

3. If both Database and Company Policy are available,
combine both into one professional answer.

4. Never make up information.

Context:

{context}

Question:

{question}

Answer:
"""

    answer = llm.invoke(prompt)

    return {

        "route": route,

        "sources": sources,

        "confidence": result["confidence"],

        "answer": answer

    }