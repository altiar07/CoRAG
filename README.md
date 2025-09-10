# CoRAG – Contextual Retrieval-Augmented Generation

CoRAG is an experimental pipeline for **improving Retrieval-Augmented Generation (RAG)** systems.  
The idea: instead of a naive “retrieve and dump into LLM” approach, CoRAG adds contextual steps like query rewriting, multi-hop retrieval, and reranking to make responses more accurate and less noisy.   

---

## Why CoRAG?
Most RAG implementations fail in two common cases:
1. **Weak queries** → the retriever doesn’t return anything useful.  
2. **Shallow retrieval** → the answer requires reasoning over multiple chunks.  

CoRAG tries to address these with:
- Query rewriting (LLM reformulates weak/underspecified questions).  
- Multi-hop retrieval (re-queries with intermediate results).  
- Confidence scoring (“I don’t know” when retrieval is weak).  
- Embedding + reranker experiments.  

---

## Current Status
**Baseline RAG – DONE**
- [x] FAISS retriever with SentenceTransformers (MiniLM baseline).  
- [x] Local LLM integration (Phi-3 via `llama-cpp-python`, Q4 quantized).  
- [x] End-to-end pipeline with PDF ingestion (manual run).  
- [x] Interactive terminal chat (no reloading the model each time).  
- [ ] Batch PDF ingestion → next step.  

Next up: **CoRAG Foundations**
- Query rewriter module.  
- Multi-hop retrieval loop.  
- Benchmark baseline RAG vs CoRAG on a sample dataset.  

---

## Project Structure
```
CoRAG/
├── data/                # PDFs and datasets
├── models/              # locally stored LLM weights
├── src/
│   ├── retriever.py     # FAISS integration
│   ├── generator.py     # llama-cpp wrapper
│   ├── corag_chain.py   # RAG pipeline orchestration
│   └── utils.py         # helpers (chunking, preprocessing)
└── README.md
```

---

## Setup

### Requirements
- Python 3.10+
- `pip install -r requirements.txt`
- Local LLM weights (https://huggingface.co/microsoft/Phi-3-mini-4k-instruct)  
- FAISS, SentenceTransformers, llama-cpp-python

### Run
```bash
# Ingest PDF into FAISS
python src/retriever.py --ingest data/sample.pdf

# Start RAG chat loop
python src/pipeline.py
```

---

## Roadmap

- 1: Baseline RAG (done)  
- 2: CoRAG (query rewriting, multi-hop retrieval)  
- 3: Scaling (GPU offload, Kaggle tests on 7B+ models)  
- 4: Robustness (confidence scoring, reranker, embeddings benchmark)  
- 5: API & UI (FastAPI backend + Streamlit/Gradio)  
- 6: Evaluation & Docs (benchmarks, Hugging Face demo, full docs)  

---

## References
- [SentenceTransformers](https://www.sbert.net/)  
- [FAISS](https://faiss.ai/)  
- [llama-cpp-python](https://github.com/abetlen/llama-cpp-python)  
- [RAG Survey (Lewis et al., 2020)](https://arxiv.org/abs/2005.11401)  

---

## 👤 Author
Tushar Ranjan – MSc Embedded Systems @ University of Freiburg
