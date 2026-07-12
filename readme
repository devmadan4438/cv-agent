# Boundaryless AI Resume Agent

An AI-powered Resume Question Answering system built using **FastAPI**, **LangGraph**, **LangChain**, **FAISS**, and **Local Embeddings**. The application parses a resume, extracts structured metadata, builds a vector index, and allows users to ask natural language questions about the uploaded resume through an AI agent.

---

# Features

- Resume upload (PDF/DOCX)
- Resume parsing
- Section detection
- Metadata extraction
- Semantic chunking
- Local embeddings
- FAISS vector store
- Agentic RAG using LangGraph
- Tool Calling
- Streaming responses
- LangSmith tracing
- CLI support
- FastAPI REST APIs

---

# Architecture

```
Flow 1:

Resume upload > Resume Parser > Section Detector > Metadata Extractor > Chunk builder > Embedding Generator > FAISS DB 

Flow 2:
User Query > Agent > Check Routing for Reqwrite query OR Standalone Node > Tool Selection >  Repeat > Final Answer
```

---

# Tech Stack

## Backend

- Python 3.11+
- FastAPI
- Uvicorn

## AI

- LangChain
- LangGraph
- LangSmith
- Groq LLM - Free Tier

## LLM serve
- Ollama

## Embeddings

- nomic-embed-text (open source model)


## Vector Database

- FAISS

## Resume Parsing

- PyMuPDF (fitz)

---

# Supported Files

Supported formats

- PDF
- DOCX

---
# API

## Upload Resume

```
POST /api
```

Response

```json
{
  "success": true,
  "message": "You are ready to ask questions about your CV",
  "data": {
    "session_id": "xxxxxxxx"
  }
}
```

---

# CLI

Run

```bash
python -m app.cli
```

Example

```
[Agent] > Please enter session id:

abc123

[You] >
Tell me about my projects

[Agent]
...
```

---
# Running Locally

Create virtual environment

```bash
python -m venv venv
```

Activate

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run API

```bash
python -m app.main
```

Run CLI

```bash
python -m app.cli
```

# Author

Madan Mohan

Senior Software Engineer

Python | FastAPI | React | LangGraph | GenAI