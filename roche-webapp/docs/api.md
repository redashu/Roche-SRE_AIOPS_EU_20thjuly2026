# API Documentation

## Overview

ChatApp exposes a web interface implemented using Flask.

The application currently provides three HTTP endpoints.

---

# Technology

| Component      | Value         |
| -------------- | ------------- |
| Framework      | Flask         |
| Protocol       | HTTP          |
| Data Format    | HTML          |
| AI Provider    | OpenAI        |
| Authentication | Session-based |

---

# API Endpoints

| Method     | Endpoint | Purpose     |
| ---------- | -------- | ----------- |
| GET / POST | /        | User Login  |
| GET / POST | /home    | AI Chat     |
| POST       | /logout  | User Logout |

---

# Endpoint Details

## 1. Login

### URL

```text
/
```

### Methods

```text
GET
POST
```

### Description

Displays the login page and authenticates the user.

---

### Form Parameters

| Parameter | Type   | Required |
| --------- | ------ | -------- |
| username  | String | Yes      |
| password  | String | Yes      |

---

### Success Flow

```text
Browser

↓

POST /

↓

Validate User

↓

MySQL

↓

Create Session

↓

Redirect /home
```

---

### Failure

Returns:

```text
Invalid username or password
```

---

# 2. Home (AI Chat)

### URL

```text
/home
```

### Methods

```text
GET
POST
```

### Description

Displays the chat interface and communicates with the OpenAI API.

---

### Form Parameters

| Parameter  | Type   | Required |
| ---------- | ------ | -------- |
| user_input | String | Yes      |

---

### Request Flow

```text
User

↓

Flask

↓

Load History

↓

OpenAI

↓

Generate Response

↓

Save Conversation

↓

Render HTML
```

---

### Processing Steps

1. Verify user session.
2. Read chat history.
3. Save user message.
4. Send request to OpenAI.
5. Receive AI response.
6. Save AI response.
7. Render Markdown.
8. Display response.

---

# 3. Logout

### URL

```text
/logout
```

### Method

```text
POST
```

### Description

Clears the Flask session and redirects the user to the login page.

---

### Flow

```text
User

↓

POST /logout

↓

Clear Session

↓

Redirect /
```

---

# Authentication

Authentication uses Flask sessions.

Session values:

```text
logged_in
user_id
username
fullname
role
chat_session_id
history
```

---

# Database Calls

Login

```text
users
```

Chat Session

```text
chat_sessions
```

Conversation Storage

```text
chat_messages
```

---

# OpenAI Integration

Current Model

```text
gpt-4o-mini
```

Current API

```text
Chat Completions API
```

Conversation history is sent with every request to maintain context.

---

# Response Rendering

The application converts Markdown responses into HTML before displaying them.

Library used:

```text
markdown2
```

Supported features:

* Headings
* Tables
* Bullet Lists
* Numbered Lists
* Code Blocks
* Inline Code
* Bold
* Italics

---

# HTTP Status Behaviour

| Scenario         | Behaviour             |
| ---------------- | --------------------- |
| Valid Login      | Redirect to `/home`   |
| Invalid Login    | Display error message |
| Session Expired  | Redirect to `/`       |
| OpenAI Failure   | Display error message |
| Database Failure | Application error     |

---

# Current Limitations

* No REST API
* No JSON endpoints
* No JWT authentication
* No user registration
* No password reset
* No streaming responses
* No file upload
* No API versioning

---

# Planned API Enhancements

* REST API
* JSON responses
* JWT authentication
* Chat history endpoint
* New chat endpoint
* Delete conversation endpoint
* User profile endpoint
* Health endpoint
* Metrics endpoint
* AI model configuration endpoint

---

# API Summary

Current application capabilities:

* User authentication
* AI chat interface
* Persistent conversations
* Session management
* OpenAI integration
* Database-backed conversation history
