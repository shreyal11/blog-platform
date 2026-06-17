🚀 Dockerized Blog Platform (3-Tier Application)

A full-stack blog application built using Flask, MySQL, and Docker.
This project demonstrates a complete 3-tier architecture with full CRUD functionality and containerized deployment.

🧠 Features
📝 Create blog posts
📖 View all posts
✏️ Edit posts
🗑️ Delete posts
🐳 Fully containerized using Docker
🔗 MySQL database integration
⚡ Docker Compose for multi-container setup
🏗️ Architecture
Frontend (HTML/CSS)
        ↓
Flask (Python Backend)
        ↓
MySQL Database
⚙️ Tech Stack
Python (Flask)
MySQL
HTML / CSS
Docker
Docker Compose
Linux (Kali/Ubuntu)
📂 Project Structure
blog-platform/
│
├── backend/
│   ├── app.py
│   ├── templates/
│   ├── static/
│   ├── Dockerfile
│   └── requirements.txt
│
├── database/
│   └── init.sql
│
└── docker-compose.yml
🚀 How to Run This Project
1️⃣ Clone the repository
git clone <your-repo-link>
cd blog-platform
2️⃣ Start the application
docker-compose up --build -d
3️⃣ Open in browser
http://localhost:5000
📌 What I Learned
Docker containerization
Flask backend development
MySQL integration
CRUD operations
Linux command line
Multi-container architecture using Docker Compose
👩‍💻 Author

Shreya Lokhande

⭐ Future Improvements
Add Nginx reverse proxy
Improve UI with Bootstrap
Add authentication system (login/signup)
Deploy on cloud (AWS / Render)
