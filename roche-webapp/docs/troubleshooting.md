ncident ID: INC-001

Problem

MySQL Pod remained Pending
PVC remained Pending

Symptoms

kubectl get pvc → Pending
kubectl get pv → No resources found

Verification

kubectl describe pvc mysql-pvc

Observed Event

Waiting for a volume to be created either by the external provisioner 'ebs.csi.aws.com'

Root Cause

EKS cluster did not have an associated IAM OIDC provider, preventing installation of the EBS CSI driver.

We'll continue documenting the rest of the incident once the CSI driver is installed and the PVC becomes Bound.

Incident: MySQL Pod stuck in Pending

Symptoms

Pod remained Pending
PVC remained Pending
No PV created

Investigation

kubectl describe pvc mysql-pvc

Found:

Waiting for a volume to be created either by the external provisioner 'ebs.csi.aws.com'

Checked:

kubectl get pods -n kube-system | grep ebs

No EBS CSI pods.

Checked:

aws eks list-addons

aws-ebs-csi-driver missing.

Associated IAM OIDC provider.
Created IAM Service Account.
First add-on installation failed due to ConfigurationConflict.
Deleted failed add-on.

Recreated with:

--resolve-conflicts OVERWRITE
Verified:
EBS CSI Controller Running
EBS CSI Node Running
Add-on status = ACTIVE

## 
# Troubleshooting Guide

This document captures the issues encountered while deploying the Flask AI Chat Application on Amazon EKS and the resolutions applied.

---

# 1. PVC Stuck in Pending

### Problem
```
kubectl get pvc

STATUS: Pending
```

### Root Cause
The Amazon EBS CSI Driver was not installed correctly, so Kubernetes was unable to dynamically provision an EBS volume.

### Resolution

Verify StorageClass

```bash
kubectl get storageclass
```

Check PVC events

```bash
kubectl describe pvc mysql-pvc
```

Install the EBS CSI Driver with the correct IAM Role

```bash
aws eks create-addon \
  --cluster-name my-cluster \
  --addon-name aws-ebs-csi-driver \
  --service-account-role-arn <ROLE_ARN> \
  --resolve-conflicts OVERWRITE
```

Verify

```bash
kubectl get pods -n kube-system | grep ebs
```

Expected

```
ebs-csi-controller   Running
ebs-csi-node         Running
```

---

# 2. EBS CSI Driver Addon Failed

### Problem

```
ConfigurationConflict
```

### Root Cause

A ServiceAccount already existed from a previous installation.

### Resolution

Delete the failed addon

```bash
aws eks delete-addon \
--cluster-name my-cluster \
--addon-name aws-ebs-csi-driver
```

Recreate with overwrite

```bash
aws eks create-addon \
--resolve-conflicts OVERWRITE
```

Verify

```bash
aws eks describe-addon \
--cluster-name my-cluster \
--addon-name aws-ebs-csi-driver
```

Expected

```
ACTIVE
```

---

# 3. MySQL Pod Running but Database Empty

### Problem

Application login failed because required tables were missing.

Example

```
chat_sessions doesn't exist
```

### Resolution

Copy schema

```bash
kubectl cp chatapp_schema.sql roche-db-pod:/tmp/
```

Import

```bash
kubectl exec -it roche-db-pod -- bash

mysql -uroot -p

use chatapp;

source /tmp/chatapp_schema.sql;
```

Verify

```sql
show tables;
```

---

# 4. Flask Deployment Cannot Connect to MySQL

### Root Cause

Incorrect environment variables.

### Resolution

Store configuration in ConfigMap

```
DB_HOST
DB_PORT
DB_NAME
```

Store credentials in Secret

```
DB_USER
DB_PASSWORD
OPENAI_API_KEY
```

Verify

```bash
kubectl exec -it <app-pod> -- env
```

---

# 5. Login Successful but Chat History Missing

### Root Cause

Only the raw message was loaded from MySQL while the template expected rendered HTML.

### Resolution

Render Markdown when loading chat history from the database before sending it to the template.

---

# 6. Chat History Lost After Logout

### Expected Behaviour

Logout clears only the browser session.

Chat history remains stored in MySQL.

After logging in again, previous conversations are reloaded from the database.

---

# 7. Flask Pod CrashLoopBackOff

### Verify Logs

```bash
kubectl logs <pod-name>
```

Common causes

- Wrong environment variables
- Database connection failure
- Missing OpenAI API Key
- Python dependency missing

---

# 8. Verify MySQL Connectivity

Inside the Flask Pod

```bash
kubectl exec -it <app-pod> -- bash
```

Test DNS

```bash
ping roche-db
```

Test MySQL

```bash
mysql -h roche-db \
-u appuser \
-p
```

---

# 9. Verify Kubernetes Objects

Pods

```bash
kubectl get pods
```

Services

```bash
kubectl get svc
```

PVC

```bash
kubectl get pvc
```

Deployments

```bash
kubectl get deployment
```

---

# 10. Chat Window Not Auto Scrolling

### Problem

New AI responses appeared below the visible area.

### Resolution

Configure the chat container as the only scrollable section and automatically scroll to the bottom after page rendering.

---

# 11. Useful Debug Commands

Describe Pod

```bash
kubectl describe pod <pod>
```

View Logs

```bash
kubectl logs <pod>
```

Shell into Pod

```bash
kubectl exec -it <pod> -- bash
```

Check Environment Variables

```bash
kubectl exec -it <pod> -- env
```

Check PVC

```bash
kubectl get pvc
```

Check StorageClass

```bash
kubectl get storageclass
```

Check Events

```bash
kubectl get events --sort-by=.metadata.creationTimestamp
```

---

# Lessons Learned

- Use ConfigMaps for application configuration.
- Store passwords and API keys in Kubernetes Secrets.
- Persist chat history in MySQL rather than Flask sessions.
- Install and verify the Amazon EBS CSI Driver before creating PersistentVolumeClaims.
- Verify IAM roles, OIDC configuration, and addon health before troubleshooting storage.
- Use Kubernetes logs and events as the primary source for debugging deployment issues.
- Keep database schema under version control for easy recovery and repeatable deployments.

# 12. Chat UI & CSS Improvements

The chat interface was redesigned to provide a modern ChatGPT-style experience while keeping the layout responsive and maintainable.

## Layout Improvements

- Converted the application into a full-height (`100vh`) flex layout.
- Fixed the navigation bar at the top.
- Fixed the input area at the bottom.
- Made only the chat history section scrollable.

```css
.page {
    height: 100vh;
    display: flex;
    flex-direction: column;
    overflow: hidden;
}

.chat-area {
    flex: 1;
    overflow-y: auto;
    min-height: 0;
}
```

---

## Background Blur Layer

A transparent overlay is used to improve text readability while preserving the background image.

```css
.page::before {
    content: "";
    position: absolute;
    inset: 0;
    background: rgba(255,255,255,0.82);
    backdrop-filter: blur(2px);
}
```

---

## Chat Bubble Design

Two different message styles are used.

### User Message

- Right aligned
- Pink background
- Rounded bubble

```css
.bubble-user {
    align-self: flex-end;
    max-width: 70%;
    background: var(--pink);
    color: white;
}
```

### AI Message

- Full-width card
- White background
- Markdown friendly
- Code block support

```css
.bubble-ai {
    align-self: stretch;
    background: white;
    border: 1px solid var(--border);
}
```

---

## Markdown Rendering

AI responses support GitHub-style Markdown rendering including:

- Headings
- Lists
- Tables
- Code blocks
- Inline code
- Blockquotes
- Hyperlinks
- Horizontal rules

Markdown is converted on the server using:

```python
markdown2.markdown(
    ai_response,
    extras=[
        "fenced-code-blocks",
        "tables",
        "strike",
        "break-on-newline"
    ]
)
```

---

## Responsive Input Box

The message input automatically expands as the user types.

Features:

- Starts as a single line
- Expands automatically
- Maximum height of approximately five lines
- Internal scrolling after maximum height

---

## Voice Input

Browser Speech Recognition API is integrated.

Features:

- Microphone button
- Speech-to-text
- Automatic insertion into the message box
- Recording animation

---

## Automatic Chat Scrolling

The chat window automatically scrolls to the newest message after page load and after every conversation update, ensuring users always see the latest response.

---

## Responsive Design

The interface has been tested for:

- Desktop browsers
- Laptop screens
- Tablet devices
- Mobile screens

Responsive components include:

- Navigation bar
- Chat bubbles
- Markdown rendering
- Input area
- Buttons

---

## UI Improvements Summary

- Modern ChatGPT-inspired layout
- Persistent bottom input bar
- Scrollable chat history
- Markdown support
- Syntax-highlight-friendly code blocks
- Responsive design
- Voice input support
- Glassmorphism navigation and footer
- Background image with blur overlay
- Clean typography using **Syne** and **DM Sans**