from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from app.faiss_handler import get_best_match

app = FastAPI(
    title="LEAPBot",
    description="Chatbot for MyLEAP",
    version="1.0.1"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

 
@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    query = data.get("query", "")
 
    matches = get_best_match(query, top_k=3)
 
    if not matches:
        return {
            "response": "Sorry, I couldn't find a matching answer.",
            "similar_questions": []
        }
 
    return {
        "response": matches[0]['answer'],  # This is the answer
        "similar_questions": [m['question'] for m in matches[1:]]  # Suggestions
    }
