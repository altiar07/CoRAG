# CoRAG Demo – Baseline RAG Implementation

This repository contains the **baseline Retrieval-Augmented Generation (RAG)** pipeline that will be extended into a full **Chain-of-Retrieval Augmented Generation (CoRAG)** system.

The goal is to demonstrate **multi-hop retrieval and reasoning** with a local LLM running on Apple Silicon (M1/M2) using [`llama-cpp-python`](https://github.com/abetlen/llama-cpp-python) and quantized GGUF models.

---

## 📂 Project Structure

```plaintext
corag-demo/
│── data/                 # Sample docs (domain PDFs, txt files)
│   └── sample_docs.txt
│── models/               # Quantized GGUF model files
│   └── phi-3-mini-4k-instruct.Q4_K_M.gguf
│── notebooks/            # For experiments & prototyping
│── src/
│   ├── retriever.py       # Document embedding & retrieval
│   ├── generator.py       # LLM interface
│   ├── corag_chain.py     # Multi-step retrieval logic (to be built)
│   ├── evaluator.py       # Benchmark & evaluation functions
│   └── utils.py           # Helper functions
│── app.py                 # Streamlit/Gradio demo
│── requirements.txt
│── README.md
