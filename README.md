# rag-project
# 📌 RAG POC – Intelligent Query Answering System

## 🧠 Overview
This project is a Retrieval-Augmented Generation (RAG) system that answers user queries using:

- Structured database (employee/factual data)
- Document-based retrieval (PDF/text knowledge base)
- Hybrid search (DB + Documents)

It also includes query routing and confidence scoring to improve response quality.

---

## 🚀 Features

- Smart Query Router (DB / Docs / Hybrid / Greeting detection)
- Document-based QA using RAG pipeline
- Structured database query support
- Hybrid search (DB + Docs results)
- Confidence score for response reliability
- FastAPI backend support
- Safe response handling (no crashes)

---

## 🏗️ Architecture

User Query  
→ Query Router  
→ DB / Docs / Hybrid  
→ Retriever (Search / Embeddings)  
→ LLM Response Generator  
→ Final Answer + Confidence Score  

---

## 📂 Project Structure

RAG_POC/
├── app.py # Streamlit UI
├── rag_api.py # FastAPI backend
├── query_router.py # Query classification
├── db_search.py # Database search logic
├── hybrid_search.py # Hybrid retrieval
├── ingest.py # Data ingestion pipeline
├── requirements.txt # Dependencies
