# 🚀 Dockerized Blog Platform (3-Tier Application)

A full-stack blog application built using Flask, MySQL, and Docker.  
This project demonstrates a complete **3-tier architecture** with CRUD functionality and containerized deployment using Docker Compose.

---

## 🧠 Features
- 📝 Create blog posts  
- 📖 View all posts  
- ✏️ Edit posts  
- 🗑️ Delete posts  
- 🐳 Fully containerized using Docker  
- 🔗 MySQL database integration  
- ⚡ Multi-container setup using Docker Compose  

---

## 🏗 Architecture


Frontend (HTML/CSS)
↓
Flask (Python Backend)
↓
MySQL Database


---

## ⚙ Tech Stack
- Python (Flask)
- MySQL
- HTML / CSS
- Docker
- Docker Compose
- Linux (Kali / Ubuntu)

---

## 📂 Project Structure


blog-platform/
│
├── backend/
│ ├── app.py
│ ├── templates/
│ ├── static/
│ ├── Dockerfile
│ └── requirements.txt
│
├── database/
│ └── init.sql
│
└── docker-compose.yml


---

## 🚀 How to Run This Project

### 1️⃣ Clone the repository
```bash
git clone https://github.com/shreyal11/blog-platform.git
cd blog-platform
2️⃣ Start the application
docker-compose up --build -d
3️⃣ Open in browser
http://localhost:5000
📌 What I Learned
Docker containerization
Multi-container orchestration using Docker Compose
Flask backend development
MySQL integration with applications
Linux-based development workflow
⭐ Future Improvements
Add user authentication
Deploy on AWS / EC2
Add CI/CD pipeline using GitHub Actions
Add UI framework (Bootstrap / React)
👩‍💻 Author

Shreya Lokhande 
