# 🧠 CoRAG: Chain-of-Retrieval Augmented Generation

A local Retrieval-Augmented Generation (RAG) pipeline, extended with **multi-hop retrieval (CoRAG)** to improve question answering accuracy.  
Runs fully offline on your machine using **llama-cpp-python**, **SentenceTransformers**, and **FAISS**.

---

## 🚀 Features
- **Baseline RAG** (done)
  - Embed documents with SentenceTransformers
  - Retrieve top-k relevant chunks using FAISS
  - Feed retrieved context into a local LLM (Phi-3 Mini)
- **Interactive Chat Mode**
  - Ask multiple questions in one session (model loads once)
- **Concise Answers**
  - No extra commentary or hallucinated Q&A
- **Offline First**
  - No API calls required; everything runs locally

---
## 📂 Project Structure
---


## ⚡ Quickstart

### 1. Install
```bash
git clone <CoRAG>
cd CoRAG
pip install -r requirements.txt
```

### 2. Download model
models/phi-3-mini-4k-instruct.Q4_K_M.gguf

### 3. Add Data
Drop .pdf or .txt into data/
They are auto-ingested.

### 4. Run
python app.py
