from fastapi import FastAPI

app = FastAPI(title="Multimodal RAG System")

@app.get("/")
def home():
    return {"message": "Multimodal RAG System Running"}
