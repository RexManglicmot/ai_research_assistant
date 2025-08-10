# Status

![status](https://img.shields.io/badge/status-actively--developed-yellowgreen)

This project is **currently** being developed and improved with additional features and testing.

## Inspiration

During my undergrad and grad studies, we were given enormous stacks on stacks of papers to read. A bit too much! Hours were spent reading to prepare for lecture. A fellow grad student of mine told me that is impossible to read everything and recommended to skim for main points, which I ultimately did. Although this skill was useful back then, I wish there was a tool that would allow synthesize main findings. Thus, the inspiration for this particular project. 

# Introduction

This project is meant to be a **production-style code** Retrieval-Augmented Generation (RAG) model that lets users query one or more research papers in natural language. The assistant uses a free Hugging Face-hosted large language model (mistralai/Mistral-7B-Instruct-v0.2) and FAISS-powered semantic search to generate answers grounded in the content of uploaded PDFs.

## Metrics

This project will focus on the 4 generation metrics proposed by[Langchain](https://docs.smith.langchain.com/evaluation/tutorials/rag) and using LLM as a Judge concept that assess and score outputs like answers and summaries against specific guidelines. It acts as an automated evaluator that would otherwise require human review. The gold standard is to have a human evaluator score as well, and compare and contrast the scores of the Judge and Human, but that is outside this project scope and could be a potential follow up project.

1. **Correctness** – Accuracy vs. a gold/reference answer. *(Requires reference)*
2. **Relevance** – How well the answer addresses the question.
3. **Groundedness** – Whether all claims are supported by retrieved context (no hallucinations).
4. **Retrieval Relevance** – How relevant retrieved chunks are to the question.

**Scoring Rubric:**

| Score | Meaning |
|-------|---------|
| **5** | Perfect – fully correct/relevant/grounded |
| **4** | Good – minor issues only |
| **3** | Fair – noticeable gaps or noise |
| **2** | Poor – significant errors or irrelevance |
| **1** | Very poor – mostly wrong/off-topic |
| **0** | Invalid – empty, refusal, or broken output |

**Overall Score Calculation:**

Overall = 0.35 \cdot \text{Correctness} + 0.25 \cdot \text{Groundedness} + 0.20 \cdot \text{Relevance} + 0.20 \cdot \text{Retrieval Relevance}


**Passing Targets:**
- Correctness ≥ **4.0**
- Groundedness ≥ **4.5**
- Relevance ≥ **4.0**
- Retrieval Relevance ≥ **4.0**

## Why This Project Matters

Help students get relevant info and be more efficient with their time.

## Tech Stack

Python · sentence-transformers · FAISS · transformers · Mistral-7B-Instruct (Hugging Face) · cosine similarity · PyMuPDF · Streamlit · pytest · logging · GitHub Actions · Docker
## Project Architecture

```text

User Query
│
├── ingestion.py → Load PDFs → extract text
│
├── utils.py → chunk text + metadata (source, page)
│
├── embeddings.py → create embeddings → build/load FAISS index
│
├── agent.py → retrieve top-K chunks via cosine similarity
│
├── agent.py → send query + context to HF LLM (Mistral-7B-Instruct)
│
├── logger_config.py → log query, retrieved docs, and output
│
├── Return → Answer + citations
│
└── evaluation/ → LLM-as-judge scores:
       • Correctness
       • Relevance
       • Groundedness
       • Retrieval Relevance

```

## Setup
TBD

## Limitations
This project works well for textual data and not optimized for images and tabular forms of data. Thus, Multimodality is another potential follow-up project. 