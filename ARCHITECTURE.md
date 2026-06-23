# Multimodal RAG Architecture

## Components

1. FastAPI Backend
2. Text Embedding Model
3. Image Embedding Model (CLIP)
4. ChromaDB Vector Database
5. Retrieval Engine
6. Generation Engine
7. Evaluation Module

## Workflow

User Query
    |
    v
FastAPI
    |
    v
Retriever
    |
    +--> Text Embeddings
    |
    +--> Image Embeddings
    |
    v
ChromaDB
    |
    v
Generator
    |
    v
Response + Citations

## Retrieval

- Text-to-Text Retrieval
- Text-to-Image Retrieval
- Cross-Modal Search

## Evaluation

- Retrieval Accuracy
- Faithfulness
- Relevance
- LLM-as-a-Judge
