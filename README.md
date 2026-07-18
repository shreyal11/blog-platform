# 🚀 Kubernetes-Based Blog Platform (3-Tier Application)

A full-stack blog application built using **Flask, MySQL, Docker, and Kubernetes**.

This project demonstrates a complete **3-tier architecture** with CRUD functionality, containerization using Docker, and deployment on Kubernetes with persistent storage.

---

## 🧠 Features

- 📝 Create blog posts
- 📖 View all posts
- ✏️ Edit posts
- 🗑️ Delete posts
- 🐳 Fully containerized using Docker
- ☸️ Deployed on Kubernetes
- 🌐 Kubernetes Service for networking
- 🔐 ConfigMap for database initialization
- 🔑 Secret for secure database credentials
- 💾 Persistent Volume (PV)
- 📦 Persistent Volume Claim (PVC)
- ♻️ Kubernetes Self-Healing
- ⚡ Multi-container architecture

---

## 🏗 Architecture

```
Browser
    │
    ▼
Kubernetes Service
    │
    ▼
Flask Deployment
    │
    ▼
MySQL Service
    │
    ▼
MySQL Deployment
    │
    ▼
Persistent Volume Claim (PVC)
    │
    ▼
Persistent Volume (PV)
```

---

## ⚙ Tech Stack

- Python (Flask)
- MySQL
- HTML / CSS
- Docker
- Docker Compose
- Kubernetes
- Linux (Kali Linux)
- Git
- GitHub

---

## 📂 Project Structure

```
blog-platform/
│
├── backend/
│   ├── app.py
│   ├── Dockerfile
│   ├── requirements.txt
│   ├── templates/
│   └── static/
│
├── database/
│   └── init.sql
│
├── k8s/
│   ├── namespace.yaml
│   ├── deployment.yaml
│   ├── service.yaml
│   ├── mysql-deployment.yaml
│   ├── mysql-service.yaml
│   ├── configmap.yaml
│   ├── secret.yaml
│   ├── pv.yaml
│   └── pvc.yaml
│
├── docker-compose.yml
│
└── README.md
```

---

## 🚀 Run Using Docker

### Clone the repository

```bash
git clone https://github.com/shreyal11/blog-platform.git

cd blog-platform
```

### Start the application

```bash
docker-compose up --build -d
```

### Open in browser

```
http://localhost:5000
```

---

## ☸️ Run Using Kubernetes

### Create Namespace

```bash
kubectl apply -f k8s/namespace.yaml
```

### Deploy all Kubernetes resources

```bash
kubectl apply -f k8s/
```

### Verify deployment

```bash
kubectl get all -n blog-platform
```

### Access the application

```bash
kubectl port-forward service/blog-platform-service -n blog-platform 5000:5000
```

Open in browser:

```
http://localhost:5000
```

---

## ☸ Kubernetes Resources Used

- Namespace
- Deployment
- Service
- ConfigMap
- Secret
- Persistent Volume (PV)
- Persistent Volume Claim (PVC)

---

## 📌 What I Learned

- Docker containerization
- Multi-container applications using Docker Compose
- Deploying applications on Kubernetes
- Kubernetes Deployments
- Kubernetes Services
- Namespaces
- ConfigMaps
- Secrets
- Persistent Volumes (PV)
- Persistent Volume Claims (PVC)
- Self-Healing in Kubernetes
- Flask and MySQL integration
- Linux-based development workflow

---

## ⭐ Future Improvements

- Ingress Controller
- Horizontal Pod Autoscaler (HPA)
- CI/CD using Jenkins
- Monitoring with Prometheus & Grafana
- Deploy on AWS EKS

---

## 👩‍💻 Author

**Shreya Lokhande**
