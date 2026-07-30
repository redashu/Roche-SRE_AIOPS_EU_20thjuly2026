### Current Application Deployment 

```
                    Internet User
                          │
                          ▼
                AWS Load Balancer (Service)
                          │
                          ▼
                 roche-chatapp Service
                          │
                          ▼
            roche-chatapp Deployment (1 Replica)
                          │
                          ▼
                  Flask + Python Application
                          │
        ┌─────────────────┴──────────────────┐
        │                                    │
        ▼                                    ▼
    MySQL Service                    OpenAI / Bedrock API
        │                                    │
        ▼                                    ▼
  roche-db Deployment                 External LLM
        │
        ▼
 Persistent Volume Claim
        │
        ▼
 Amazon EBS Volume

Application Configuration
────────────────────────────────────────────
ConfigMaps
• app-config
• mysql-config

Secrets
• app-secret
• db-secret
• mysql-secret

```