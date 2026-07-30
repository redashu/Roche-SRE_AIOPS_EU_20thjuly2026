# Architecture Document

## Application Name

ChatApp

---

# Overview

ChatApp is a two-tier AI-powered web application developed using Flask, MySQL, and the OpenAI API.

The application provides:

* User authentication
* AI-powered chat interface
* Persistent chat history
* Conversation memory
* Session management

The application is containerized using Docker and designed for deployment on Kubernetes.

---

# Architecture

```
+-------------------+
|   Web Browser     |
+-------------------+
          |
          | HTTP
          v
+-------------------+
| Flask Application |
|     (Python)      |
+-------------------+
      |        |
      |        |
      |        +----------------------+
      |                               |
      |                               |
      v                               v
+--------------+             +------------------+
|   MySQL DB   |             |   OpenAI API     |
+--------------+             +------------------+
```

---

# Components

## 1. Web Browser

Provides the user interface.

Responsibilities:

* User Login
* Chat Interface
* Display AI Responses
* Maintain User Session

---

## 2. Flask Application

Acts as the backend application.

Responsibilities:

* User Authentication
* Session Management
* Database Operations
* OpenAI Integration
* Conversation Management

Main Technologies:

* Python
* Flask
* Markdown2
* mysql-connector-python
* OpenAI SDK

---

## 3. MySQL Database

Stores application data.

Current tables:

* users
* chat_sessions
* chat_messages

Responsibilities:

* User Authentication
* Chat Session Storage
* Conversation Persistence

---

## 4. OpenAI API

Provides Large Language Model capabilities.

Current model:

* gpt-4o-mini

Responsibilities:

* Natural Language Processing
* Multi-turn Conversation
* AI Response Generation

---

# Request Flow

## User Login

```
Browser

↓

Flask

↓

MySQL

↓

User Validation

↓

Session Created

↓

Home Page
```

---

## AI Chat Flow

```
User

↓

Flask

↓

Load Previous History

↓

OpenAI API

↓

AI Response

↓

Save Conversation

↓

Display Response
```

---

# Database Tables

```
users

↓

chat_sessions

↓

chat_messages
```

Relationships:

* One User → Many Chat Sessions
* One Chat Session → Many Messages

---

# Session Management

The application uses Flask sessions to maintain the authenticated user's state.

Session stores:

* logged_in
* user_id
* username
* fullname
* role
* chat_session_id
* history

---

# Technology Stack

| Component     | Technology            |
| ------------- | --------------------- |
| Frontend      | HTML5                 |
| Styling       | CSS3                  |
| Backend       | Python Flask          |
| AI            | OpenAI GPT-4o-mini    |
| Database      | MySQL 8               |
| Container     | Docker                |
| Orchestration | Kubernetes            |
| Configuration | Environment Variables |

---

# Current Features

* User Login
* AI Chat
* Conversation Memory
* Persistent Chat History
* Markdown Rendering
* Session Management
* Database-backed Authentication

---

# Future Enhancements

* Password Hashing
* User Registration
* Multiple Chat Conversations
* Chat Search
* Conversation Rename
* Chat Deletion
* File Upload
* Image Support
* Streaming Responses
* Role-Based Access Control
* Kubernetes Health Checks
* Monitoring
* Logging
* Horizontal Scaling

---

# High-Level Architecture

```
Browser
    │
    ▼
Flask Application
    │
    ├──────────────► MySQL Database
    │
    └──────────────► OpenAI API
```
