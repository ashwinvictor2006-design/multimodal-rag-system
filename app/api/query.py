from fastapi import APIRouter

router = APIRouter()

@router.get("/query")
async def query(question: str):
    return {
        "question": question,
        "answer": "Multimodal RAG response will be generated here."
    }
