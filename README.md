# 🚀 ML API with FastAPI, Docker, and Kubernetes

This project demonstrates how to build and deploy a Machine Learning API using:

- FastAPI (API layer)
- Scikit-learn (ML model)
- Docker (containerization)
- Kubernetes (deployment)

---

## 📁 Project Structure

## 📁 Project Structure
ml-api-k8s/
│
├── src/
│   ├── api/
│   │   ├── main.py
│   │   └── routes.py
│   │
│   ├── model/
│   │   ├── train.py
│   │   ├── predict.py
│   │   └── utils.py
│
├── artifacts/
│   └── model.pkl
│
├── k8s/
│   ├── deployment.yaml
│   └── service.yaml
│
├── Dockerfile
├── requirements.txt
└── README.md
---## ⚙️ 1. Train the Model```bashpython src/model/train.py
This creates:
artifacts/model.pkl

🌐 2. Run API locally
uvicorn src.api.main:app --reload
Open:
http://localhost:8000/docs

🐳 3. Build Docker Image
docker build -t ml-api .

▶️ 4. Run Docker Container
docker run -p 8000:8000 ml-api

☸️ 5. Deploy to Kubernetes
Start cluster:
minikube start
Build image inside Minikube:
eval $(minikube docker-env)docker build -t ml-api .
Apply configs:
kubectl apply -f k8s/deployment.yamlkubectl apply -f k8s/service.yaml

🔍 6. Access the API
minikube service ml-api-service

🔄 Workflow
Train Model → Save artifact → Load in API → Dockerize → Deploy on Kubernetes

📌 Features


ML model serving via API


Containerized deployment


Scalable with Kubernetes


Clean project structure



🚀 Future Improvements


Add MLflow tracking


Add CI/CD pipeline


Add monitoring (Prometheus + Grafana)


Add model versioning



👨‍💻 Author
Moh Rafik
[Profile](www.mohrafik.it)


---# 🔥 Final Tips (important)
- Keep `.gitignore` strict → avoid pushing large models accidentally 
- Keep `.dockerignore` lean → faster builds  
- Keep `README.md` clear   
 
