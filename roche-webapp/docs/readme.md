# ChatApp – AI Powered Enterprise Web Application

## Overview

ChatApp is a Flask-based AI web application that integrates with the OpenAI API to provide an intelligent conversational assistant.

The project was built as a realistic multi-tier application that can be deployed locally using Docker and later on Kubernetes. It is also designed to serve as the foundation for an Enterprise AI Assistant where RAG, Tool Calling, Memory, and Agentic AI capabilities can be implemented incrementally.

---

# Objectives

* Build a production-style Flask application
* Integrate OpenAI for conversational AI
* Store user authentication in MySQL
* Persist chat history in a database
* Deploy using Docker
* Deploy on Kubernetes
* Generate operational documentation for RAG
* Simulate enterprise production environments

---

# Technology Stack

| Component         | Technology  |
| ----------------- | ----------- |
| Backend           | Python      |
| Web Framework     | Flask       |
| Frontend          | HTML5, CSS3 |
| AI Provider       | OpenAI      |
| Database          | MySQL       |
| Containerization  | Docker      |
| Orchestration     | Kubernetes  |
| Future Deployment | Amazon EKS  |

---

# Features

* User Login
* Session Management
* OpenAI Chat Integration
* Conversation Memory
* Chat History Persistence
* Markdown Response Rendering
* Docker Ready
* Kubernetes Ready
* Enterprise Documentation

---

# Project Architecture

```text
                Browser
                   │
                   ▼
              Flask Web App
                   │
        ┌──────────┴──────────┐
        ▼                     ▼
     MySQL Database      OpenAI API
        │                     │
        └──────────┬──────────┘
                   ▼
             Chat Response
```

---

# Folder Structure

```text
chatapp/
│
├── app.py
├── requirements.txt
├── Dockerfile
├── .env.example
├── chatapp_schema.sql
│
├── static/
├── templates/
│
├── kubernetes/
│
├── docs/
│
├── screenshots/
│
└── README.md
```

---

# Database

Current database tables:

* users
* chat_sessions
* chat_messages

The database stores:

* User credentials
* Chat sessions
* Conversation history

---

# Application Workflow

```text
User

↓

Login

↓

MySQL Authentication

↓

Home Page

↓

Ask Question

↓

OpenAI API

↓

AI Response

↓

Store Conversation

↓

Display Response
```

---

# Documentation

The `docs/` directory contains:

* architecture.md
* deployment-guide.md
* database.md
* api.md
* runbook.md
* troubleshooting.md
* known-issues.md

---

# Deployment

Deployment targets include:

* Local Python
* Docker
* Kubernetes
* Amazon EKS (Future)

---

# Screenshots

Store application screenshots inside:

```text
screenshots/
```

Suggested screenshots:

* Login Page
* Home Page
* Chat Interface
* Docker Deployment
* Kubernetes Dashboard
* MySQL Database
* Kubernetes Pods
* Kubernetes Services

---

# Future Enhancements

* Password Hashing
* User Registration
* Multiple Chat Sessions
* Streaming Responses
* File Upload
* Tool Calling
* Retrieval-Augmented Generation (RAG)
* AI Agent
* Kubernetes Operations
* Amazon Bedrock Integration

---

# Enterprise AI Roadmap

```text
Flask Application
        │
        ▼
OpenAI Chat
        │
        ▼
Persistent Memory
        │
        ▼
Tool Calling
        │
        ▼
RAG
        │
        ▼
Enterprise AI Assistant
        │
        ▼
Agentic AI
```

---

# Learning Objectives

This project demonstrates:

* Flask Application Development
* OpenAI Integration
* Session Management
* Database Integration
* Docker Containerization
* Kubernetes Deployment
* Enterprise Documentation
* Production-Style Application Design

---

# License

This project is intended for learning, demonstrations, and enterprise AI implementation exercises.
