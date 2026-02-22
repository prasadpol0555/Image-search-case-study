print("Script started")
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

print("Loading model...")
model = SentenceTransformer("clip-ViT-B-32")

print("Loading Faiss index...")
index = faiss.read_index("data/image_index.faiss")
print("Loading image paths.....")
image_names = np.load("data/image_names.npy")

def search_images(query, top_k=5):
    query_embedding = model.encode([query]).astype("float32")
    distances, indices = index.search(query_embedding, top_k)
    return [image_names[i] for i in indices[0]]

if __name__ == "__main__":
    print(search_images("a dog playing in park"))


