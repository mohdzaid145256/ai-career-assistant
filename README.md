# 🚀 AI Career Assistant

### AI-Powered Career Development Platform

Built with **FastAPI**, **PostgreSQL**, **Google Gemini AI**, and **Docker**

ATS Analysis • Resume Intelligence • Interview Preparation • Career Optimization

---

# 📖 Overview

AI Career Assistant is a production-ready backend platform designed to help job seekers improve their resumes, evaluate ATS compatibility, prepare for interviews, and receive AI-driven career guidance.

The platform combines traditional backend engineering principles with modern Generative AI capabilities to provide intelligent career assistance through a scalable API architecture.

The system performs:

* Resume Management
* Resume Parsing
* Skill Extraction
* ATS Score Analysis
* Resume Recommendations
* AI Interview Preparation
* AI Resume Review
* AI Resume vs Job Description Matching
* Authentication & Authorization
* Dockerized Deployment

---

# 🎯 Problem Statement

Recruiters often receive hundreds of applications for a single role.

Most candidates struggle with:

* ATS optimization
* Resume quality assessment
* Interview preparation
* Identifying missing skills
* Understanding job requirements

AI Career Assistant addresses these challenges through an AI-driven platform that provides actionable career insights.

---

# ✨ Key Features

## 🔐 Authentication System

* JWT Authentication
* Secure Login
* Protected Routes
* User Authorization

---

## 📄 Resume Management

* Resume Upload
* Resume Storage
* Resume Retrieval
* Resume Tracking

---

## 📑 PDF Resume Parsing

Extracts content from uploaded resumes.

Supports:

* PDF Documents
* Resume Text Extraction
* Resume Processing Pipeline

---

## 🧠 Skill Extraction Engine

Automatically identifies technical skills from resumes.

Examples:

* Python
* FastAPI
* SQL
* PostgreSQL
* Docker
* AWS
* TensorFlow
* Machine Learning
* Kubernetes
* Redis
* Terraform
* LangChain
* OpenAI

---

## 📊 ATS Scoring Engine

Calculates ATS compatibility by comparing:

Resume Skills

VS

Job Description Skills

Outputs:

* ATS Score
* Matched Skills
* Missing Skills

---

## 💡 Resume Recommendation Engine

Provides improvement suggestions such as:

* Missing Technologies
* Resume Enhancement Opportunities
* Skill Gap Analysis

---

## 🎤 Interview Question Generator

Generates interview questions for:

* Python
* FastAPI
* Docker
* AWS
* Machine Learning

and more.

---

## 🤖 AI Interview Answer Generator

Powered by Google Gemini.

Generates professional answers for:

* Technical Questions
* Backend Questions
* Cloud Questions
* AI/ML Questions

Example:

Question:

"What is FastAPI Dependency Injection?"

Output:

AI-generated professional interview answer.

---

## 📝 AI Resume Review Engine

Analyzes resumes and provides:

* Overall Assessment
* Strengths
* Weaknesses
* Resume Improvements

Powered by Google Gemini.

---

## 🎯 AI Resume vs Job Description Match Engine

Compares:

Resume

VS

Job Description

Outputs:

* Match Score
* Missing Skills
* Strengths
* Improvement Recommendations

---

# 🏗️ System Architecture

```text
                    User
                      │
                      ▼
               FastAPI API
                      │
                      ▼
            Authentication Layer
                      │
                      ▼
              Service Layer
                      │
        ┌─────────────┼─────────────┐
        ▼             ▼             ▼
 Resume Engine    ATS Engine    AI Engine
        │             │             │
        ▼             ▼             ▼
 PostgreSQL      Skill Engine    Gemini AI
        │
        ▼
    Database
```

---

# ⚙️ Technology Stack

## Backend

* Python 3.12
* FastAPI
* Uvicorn

## Database

* PostgreSQL
* SQLAlchemy ORM
* Alembic

## Authentication

* JWT
* Passlib
* Python-JOSE

## AI

* Google Gemini 2.5 Flash
* Resume Intelligence Engine
* ATS Analysis Engine

## File Processing

* PyMuPDF

## Deployment

* Docker
* Docker Desktop

---

# 📂 Project Structure

```text
ai-career-assistant/

├── api/
│   └── v1/
│       ├── auth.py
│       ├── resume.py
│       ├── ats.py
│       ├── interview.py
│       ├── interview_answer.py
│       ├── resume_review.py
│       └── resume_match.py
│
├── models/
├── repositories/
├── services/
├── schemas/
├── database/
├── alembic/
├── uploads/
├── Dockerfile
├── requirements.txt
├── .env
└── main.py
```

---

# 📡 API Modules

| Module            | Description          |
| ----------------- | -------------------- |
| Authentication    | Login & JWT          |
| Resume            | Resume Management    |
| ATS               | ATS Analysis         |
| Interview         | Interview Questions  |
| Interview Answers | AI Interview Answers |
| Resume Review     | AI Resume Review     |
| Resume Match      | AI Resume Matching   |

---

# 🐳 Docker Support

Build:

```bash
docker build -t ai-career-assistant .
```

Run:

```bash
docker run -p 8000:8000 --env-file .env ai-career-assistant
```

---

# 🚀 Local Setup

Clone:

```bash
git clone https://github.com/mohdzaid145256/ai-career-assistant.git
cd ai-career-assistant
```

Create Virtual Environment:

```bash
python -m venv venv
source venv/bin/activate
```

Install Dependencies:

```bash
pip install -r requirements.txt
```

Run Server:

```bash
uvicorn main:app --reload
```

---

# 📘 API Documentation

FastAPI Swagger UI:

```text
http://localhost:8000/docs
```

ReDoc:

```text
http://localhost:8000/redoc
```

---

# 🔥 Major Milestones

✅ JWT Authentication

✅ Resume Upload System

✅ PostgreSQL Integration

✅ PDF Parsing Pipeline

✅ Skill Extraction Engine

✅ ATS Scoring Engine

✅ Resume Recommendation Engine

✅ Interview Question Generator

✅ AI Interview Answers (Gemini)

✅ AI Resume Review Engine

✅ AI Resume Match Engine

✅ Docker Containerization

---

# 🛣️ Future Roadmap

* Resume Builder
* Multi-Resume Support
* Cover Letter Generator
* AI Career Coach
* Job Recommendation Engine
* LinkedIn Profile Analysis
* Vector Search
* RAG-Based Career Assistant
* Kubernetes Deployment
* CI/CD Pipeline

---

# 👨‍💻 Author

**Mohd Zaid**

GitHub:

https://github.com/mohdzaid145256

---

# ⭐ Project Vision

To build a complete AI-powered career development ecosystem that helps candidates improve their resumes, prepare for interviews, optimize ATS scores, and make better career decisions using modern AI technologies.

