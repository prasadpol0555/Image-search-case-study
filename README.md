# 🖼️ AI-Powered Semantic Image Search System

An enterprise-grade visual search system that enables users to retrieve relevant images using natural language queries. The system uses multimodal embeddings and vector search for fast and scalable image retrieval.

--------------------------------------

## 🚀 Features

- 🔎 Semantic Image Search (Text → Image)
- 🧠 CLIP-based multimodal embeddings
- ⚡ FAISS vector database for fast retrieval
- 📝 AI-generated explanations for search results
- 🌐 FastAPI backend with HTML frontend
- 🐳 Dockerized for production deployment

---------------------------------------

## 🏗️ System Architecture

User → FastAPI → Text Embedding → FAISS Search → Top 5 Results → Explanation → UI

----------------------------------------

## 📂 Project Structure

IMAGE-SEARCH/
│
├── data/
│   ├── images/
│   ├── image_index.faiss
│   └── image_names.npy
│
├── scripts/
│   ├── download_images.py
│   └── image_embeddings.py
│
├── templates/
│   └── index.html
│
├── app.py
├── search.py
├── explanation.py
├── requirements.txt
├── Dockerfile
└── README.md

----------------------------------

## 🧠 Tech Stack

- FastAPI
- SentenceTransformers (CLIP)
- FAISS
- NumPy
- Docker
- HTML

---------------------------------------------

## 🛠️ Setup Instructions (Without Docker) 

1️⃣ Create virtual environment

python -m venv venv  
venv\Scripts\activate  

2️⃣ Install dependencies

pip install -r requirements.txt  

3️⃣ Run server

uvicorn app:app  

Open: http://127.0.0.1:8000

-----------------------------------------

## 🐳 Run With Docker (Recommended)

Clone the Git Repository:

git clone <repo_url>
cd ai-image-search-casestudy

Build image:

docker build -t image-search .

Run container:

docker run -p 8000:8000 image-search

Open :

http://localhost:8000

-------------------------------------------------

## 📈 Future Improvements

- GPU acceleration
- Redis caching
- Scalable FAISS indexing
- Cloud deployment (AWS/GCP/Azure)
- Kubernetes orchestration

---------------------------------------------------------------------------
-------------------------------------------------------------------------------------