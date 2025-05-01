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
        "question" : matches[0]['question'],  # This is the question
        "response": matches[0]['answer'],  # This is the answer
        "similar_questions": [m['question'] for m in matches[1:]]  # Suggestions
    }

@app.get("/info")
async def get_info():
    return {
        "description": "This is the LEAPBot API. Use the POST /chat endpoint to get responses based on your query.",
        "POST /chat payload": {
            "query": "Your question here"
        },
        "POST /chat response": {
            "question": "The matched question from the database",
            "response": "The corresponding answer",
            "similar_questions": ["Similar question 1", "Similar question 2"]
        }
    }
