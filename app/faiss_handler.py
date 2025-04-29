import faiss
import pickle
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')

index = faiss.read_index('data/faiss_index/index')
with open('data/faiss_index/index.meta', 'rb') as f:
    questions, answers = pickle.load(f)

def get_best_match(user_query, top_k=1):
    query_vec = model.encode([user_query], convert_to_numpy=True)
    D, I = index.search(query_vec, top_k)

    results = []
    for idx in I[0]:
        results.append({
            "question": questions[idx],
            "answer": answers[idx]
        })
    return results
