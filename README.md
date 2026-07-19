# 🚀 Kubernetes Blog Platform (3-Tier Application)

A production-style **3-tier Blog Platform** built using **Flask**, **MySQL**, **Docker**, and **Kubernetes**.

This project demonstrates how a Dockerized application can be deployed on Kubernetes using Deployments, Services, ConfigMaps, Secrets, Persistent Volumes, Health Probes, Ingress, and Horizontal Pod Autoscaler (HPA).

---

## 🏗️ Architecture

```
Browser
   │
   ▼
Kubernetes Service
   │
   ▼
Flask Application (Deployment)
   │
   ▼
MySQL Database (Deployment)
   │
   ▼
Persistent Volume (PV)
```

---

## ✨ Features

- 📝 Create Blog Posts
- 📖 View Blog Posts
- ✏️ Edit Blog Posts
- 🗑️ Delete Blog Posts
- 🐳 Dockerized Application
- ☸️ Kubernetes Deployment
- 💾 Persistent MySQL Storage
- 🔐 Secrets Management
- ⚙️ ConfigMaps
- ❤️ Liveness & Readiness Probes
- 📈 Horizontal Pod Autoscaler (HPA)
- 🌐 Ingress Configuration
- 📊 Metrics Server Integration

---

## 🛠️ Tech Stack

- Python (Flask)
- MySQL
- HTML / CSS
- Docker
- Docker Compose
- Kubernetes
- Linux (Kali Linux)
- Git & GitHub

---

## ☸️ Kubernetes Resources Used

- Namespace
- Deployment
- Service
- ConfigMap
- Secret
- Persistent Volume (PV)
- Persistent Volume Claim (PVC)
- Liveness Probe
- Readiness Probe
- Resource Requests & Limits
- Metrics Server
- Horizontal Pod Autoscaler (HPA)
- Ingress

---

## 📂 Project Structure

```
blog-platform/
│
├── backend/
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
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
│   ├── pvc.yaml
│   ├── ingress.yaml
│   └── hpa.yaml
│
├── docker-compose.yml
├── Jenkinsfile
└── README.md
```

---

## 🚀 Run with Docker

Clone the repository:

```bash
git clone https://github.com/shreyal11/blog-platform.git
cd blog-platform
```

Start the application:

```bash
docker-compose up --build -d
```

Open in your browser:

```
http://localhost:5000
```

---

## ☸️ Deploy on Kubernetes

Create the namespace:

```bash
kubectl apply -f k8s/namespace.yaml
```

Deploy all Kubernetes resources:

```bash
kubectl apply -f k8s/
```

Verify resources:

```bash
kubectl get all -n blog-platform
```

Port forward the application:

```bash
kubectl port-forward service/blog-platform-service 5000:5000 -n blog-platform
```

Open:

```
http://localhost:5000
```

---

## 📈 Horizontal Pod Autoscaler

The application automatically scales based on CPU utilization.

- Minimum Replicas: **1**
- Maximum Replicas: **5**
- Target CPU Utilization: **50%**

During testing, the application successfully scaled from **1 Pod to 5 Pods** under CPU load.

---

## 💾 Persistent Storage

The MySQL database uses:

- Persistent Volume (PV)
- Persistent Volume Claim (PVC)

This ensures data remains available even if the MySQL Pod is recreated.

---

## 📚 What I Learned

- Docker Containerization
- Kubernetes Deployments
- Kubernetes Networking
- ConfigMaps & Secrets
- Persistent Storage (PV/PVC)
- Health Checks
- Resource Management
- Metrics Server
- Horizontal Pod Autoscaling
- Ingress
- Linux & Kubernetes CLI

---

## 🚀 Future Improvements

- Role-Based Access Control (RBAC)
- Helm Charts
- CI/CD with GitHub Actions or Jenkins
- Monitoring with Prometheus & Grafana
- Deploy on AWS EKS

---

## 👩‍💻 Author

**Shreya Lokhande**

GitHub: https://github.com/shreyal11
