import pandas as pd
import faiss
import pickle
from sentence_transformers import SentenceTransformer
import os

def ingest_excel():
    file_path = "data/knowledge_base.xlsx"
    index_dir = "data/faiss_index/"

    if not os.path.exists(index_dir):
        os.makedirs(index_dir)

    df = pd.read_excel(file_path)
    questions = df['Questions'].astype(str).tolist()
    answers = df['Answers'].astype(str).tolist()

    model = SentenceTransformer('all-MiniLM-L6-v2')
    embeddings = model.encode(questions, convert_to_numpy=True)

    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)

    # Save FAISS index
    faiss.write_index(index, os.path.join(index_dir, 'index'))

    # Save metadata (questions and answers)
    with open(os.path.join(index_dir, 'index.meta'), 'wb') as f:
        pickle.dump((questions, answers), f)

    print(f"Ingestion complete. {len(questions)} questions indexed.")

if __name__ == "__main__":
    ingest_excel()
