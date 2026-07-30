# Runbook

## Overview

This runbook provides operational procedures for deploying, monitoring, and recovering the ChatApp application.

---

# Application Components

```text
Flask Application
↓

MySQL Database
↓

OpenAI API
```

---

# Daily Health Checks

Verify the following:

* Flask application is running.
* MySQL database is reachable.
* User login is successful.
* OpenAI API is accessible.
* Chat messages are being stored.
* Previous conversations are loading correctly.

---

# Verify Application

Open the application.

```text
http://<application-url>:5015
```

Expected result:

* Login page loads.
* No application errors.
* Static content loads correctly.

---

# Verify Login

Test using a valid user.

Example:

```text
Username : admin
Password : admin
```

Expected result:

* Login succeeds.
* Home page opens.
* Previous conversation is available.

---

# Verify Database Connectivity

Login to MySQL.

```bash
mysql -u chatuser -p chatapp
```

Verify users.

```sql
SELECT * FROM users;
```

Verify chat sessions.

```sql
SELECT * FROM chat_sessions;
```

Verify chat messages.

```sql
SELECT * FROM chat_messages;
```

---

# Verify OpenAI Connectivity

Send a prompt.

```text
Hello
```

Expected result:

* AI generates a response.
* Response appears in the browser.
* Response is saved in the database.

---

# Verify Conversation Persistence

Steps:

1. Login.
2. Send three prompts.
3. Logout.
4. Login again.

Expected result:

* Previous conversation is restored.

---

# Backup Database

Schema only.

```bash
mysqldump --no-data chatapp > chatapp_schema.sql
```

Complete backup.

```bash
mysqldump chatapp > chatapp_backup.sql
```

---

# Restore Database

```bash
mysql -u root -p chatapp < chatapp_backup.sql
```

---

# Restart Flask Application

Local execution.

```bash
python app.py
```

Docker.

```bash
docker restart chatapp
```

Kubernetes.

```bash
kubectl rollout restart deployment chatapp
```

---

# Verify Docker

Containers.

```bash
docker ps
```

Logs.

```bash
docker logs chatapp
```

---

# Verify Kubernetes

Pods.

```bash
kubectl get pods
```

Services.

```bash
kubectl get svc
```

Deployments.

```bash
kubectl get deployments
```

PVC.

```bash
kubectl get pvc
```

Ingress.

```bash
kubectl get ingress
```

---

# View Application Logs

Docker.

```bash
docker logs -f chatapp
```

Kubernetes.

```bash
kubectl logs deployment/chatapp
```

Specific pod.

```bash
kubectl logs <pod-name>
```

---

# Verify MySQL Pod

```bash
kubectl get pods
```

Enter pod.

```bash
kubectl exec -it <mysql-pod> -- bash
```

Connect.

```bash
mysql -u chatuser -p chatapp
```

---

# Common Recovery Actions

## Restart Flask

```bash
kubectl rollout restart deployment chatapp
```

---

## Restart MySQL

```bash
kubectl rollout restart deployment mysql
```

---

## Verify PVC

```bash
kubectl describe pvc
```

---

## Verify Environment Variables

```bash
kubectl describe deployment chatapp
```

---

## Verify OpenAI API Key

Confirm the following variable exists:

```text
OPENAI_API_KEY
```

---

## Verify Database Configuration

Confirm the following values:

```text
DB_HOST
DB_PORT
DB_NAME
DB_USER
DB_PASSWORD
```

---

# Operational Checklist

Daily:

* Application accessible
* Login working
* AI responses generated
* Database connected
* Chat persistence verified

Weekly:

* Backup database
* Review container logs
* Verify PVC usage
* Verify Kubernetes events

Monthly:

* Update container image
* Upgrade dependencies
* Verify backup restoration
* Clean unused images

---

# Future Runbook Enhancements

* Health endpoint verification
* Prometheus metrics
* Grafana dashboards
* Alert handling
* Rolling update procedures
* Rollback procedures
* Disaster recovery
* Secret rotation
* Database migration procedures
* Application scaling procedures
