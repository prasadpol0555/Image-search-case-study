import os
import faiss
import numpy as np
from PIL import Image
from sentence_transformers import SentenceTransformer

print("Loading CLIP model...")
model = SentenceTransformer("clip-ViT-B-32")

image_folder = "data/images"
image_embeddings = []
image_names = []

for image_name in os.listdir(image_folder):
    image_path = os.path.join(image_folder, image_name)
    image = Image.open(image_path).convert("RGB")

    embedding = model.encode(image)
    image_embeddings.append(embedding)
    image_names.append(image_name)

image_embeddings = np.array(image_embeddings).astype("float32")

index = faiss.IndexFlatL2(image_embeddings.shape[1])
index.add(image_embeddings)

faiss.write_index(index, "data/image_index.faiss")
np.save("data/image_names.npy", image_names)

print("Embeddings created successfully!")
