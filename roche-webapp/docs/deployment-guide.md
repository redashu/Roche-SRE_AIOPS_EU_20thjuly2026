# Deployment Guide

## Overview

This document describes how to deploy the ChatApp application using Docker and Kubernetes.

The deployment consists of:

* Flask Application
* MySQL Database
* Persistent Volume
* Kubernetes Services

---

# Prerequisites

Software required:

* Docker
* Kubernetes Cluster
* kubectl
* Python 3.12
* MySQL 8
* Git

---

# Project Structure

```text
chatapp/
│
├── app.py
├── Dockerfile
├── requirements.txt
├── .env
├── chatapp_schema.sql
│
├── templates/
├── static/
│
└── kubernetes/
```

---

# Build Docker Image

```bash
docker build -t chatapp:v1 .
```

---

# Verify Image

```bash
docker images
```

---

# Run Locally

```bash
docker run -d \
--name chatapp \
-p 5015:5015 \
--env-file .env \
chatapp:v1
```

---

# Database Preparation

Create the database.

```sql
CREATE DATABASE chatapp;
```

Restore schema.

```bash
mysql -u root -p chatapp < chatapp_schema.sql
```

Insert application users.

```sql
INSERT INTO users ...
```

---

# Environment Variables

```text
OPENAI_API_KEY=<your_key>

DB_HOST=mysql-service
DB_PORT=3306
DB_USER=chatuser
DB_PASSWORD=chat123
DB_NAME=chatapp
```

---

# Kubernetes Resources

Deployment consists of:

* Namespace
* Secret
* PersistentVolumeClaim
* MySQL Deployment
* MySQL Service
* Flask Deployment
* Flask Service
* Ingress

---

# Deployment Order

Deploy resources in the following order:

1. Namespace
2. Secret
3. PersistentVolumeClaim
4. MySQL Deployment
5. MySQL Service
6. Restore Database
7. Flask Deployment
8. Flask Service
9. Ingress

---

# Verify Deployment

Pods

```bash
kubectl get pods
```

Services

```bash
kubectl get svc
```

Deployments

```bash
kubectl get deployments
```

Persistent Volume Claims

```bash
kubectl get pvc
```

Ingress

```bash
kubectl get ingress
```

---

# Application Access

Application URL

```text
http://<LoadBalancer-IP>:5015
```

or

```text
http://<Ingress-Host>
```

---

# Upgrade Application

Build a new image.

```bash
docker build -t chatapp:v2 .
```

Update Deployment.

```bash
kubectl set image deployment/chatapp \
chatapp=chatapp:v2
```

Verify rollout.

```bash
kubectl rollout status deployment/chatapp
```

---

# Rollback

```bash
kubectl rollout undo deployment/chatapp
```

---

# Backup

Export database schema.

```bash
mysqldump --no-data chatapp > chatapp_schema.sql
```

Export application data.

```bash
mysqldump chatapp > chatapp_backup.sql
```

---

# Health Checks

Verify:

* Flask pod is Running
* MySQL pod is Running
* PVC is Bound
* Flask can connect to MySQL
* Flask can reach the OpenAI API
* User login succeeds
* Chat history is saved
* Previous conversations load after login

---

# Deployment Validation Checklist

* Flask pod running
* MySQL pod running
* Services created
* PVC bound
* Database restored
* Login successful
* Chat working
* Chat persistence verified
* OpenAI connectivity verified
* Application accessible through Kubernetes
