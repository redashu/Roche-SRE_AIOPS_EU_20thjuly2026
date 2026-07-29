# Roche-SRE_AIOPS_EU_20thjuly2026

# Enterprise AI for Amazon EKS - Learning & Architecture Roadmap

```mermaid
flowchart LR

    %% =====================================================
    %% PART 1
    %% =====================================================
    subgraph P1["Part 1 - LLM Fundamentals"]
        A1["Model Discovery"]
        A2["Invoke Foundation Model"]
        A3["Chat Application"]
        A4["Conversation Memory"]
        A5["Prompt Engineering"]

        A1 --> A2
        A2 --> A3
        A3 --> A4
        A4 --> A5
    end

    %% =====================================================
    %% PART 2
    %% =====================================================
    subgraph P2["Part 2 - AI Applications"]
        B1["Tool Calling"]
        B2["Multiple Tools"]
        B3["Tool Registry"]
        B4["LLM Tool Selection"]

        subgraph Tools["Enterprise Tools"]
            T1["Kubernetes Tool"]
            T2["CloudWatch Tool"]
        end

        B5["Prompt → Tool → Response"]

        B1 --> B2
        B2 --> B3
        B3 --> B4
        B4 --> T1
        B4 --> T2

        T1 --> B5
        T2 --> B5
    end

    %% =====================================================
    %% PART 3
    %% =====================================================
    subgraph P3["Part 3 - Enterprise AI"]
        C1["Retrieval-Augmented Generation (RAG)"]
        C2["AI Workflows"]
        C3["AI Agents"]
        C4["Multi-Agent System"]
        C5["Enterprise AI-Ops Platform"]

        C1 --> C2
        C2 --> C3
        C3 --> C4
        C4 --> C5
    end

    %% =====================================================
    %% KNOWLEDGE SOURCES
    %% =====================================================
    subgraph Knowledge["Enterprise Knowledge Sources"]
        K1["Runbooks"]
        K2["GitHub"]
        K3["Confluence"]
        K4["Jira"]
        K5["Terraform"]
        K6["Helm Charts"]
        K7["Kubernetes YAML"]
        K8["Internal Documentation"]
    end

    %% =====================================================
    %% TARGET PLATFORM
    %% =====================================================
    subgraph AWS["Amazon EKS Environment"]
        E1["Applications"]
        E2["Pods"]
        E3["Deployments"]
        E4["Services"]
        E5["Ingress"]
        E6["Namespaces"]
        E7["Nodes"]
    end

    %% =====================================================
    %% FLOW
    %% =====================================================
    P1 --> P2
    P2 --> P3

    Knowledge --> C1

    C5 --> T1
    C5 --> T2

    T1 --> AWS
    T2 --> AWS

    AWS --> R1["Detect Anomalies"]
    AWS --> R2["Root Cause Analysis"]
    AWS --> R3["Predictive Insights"]
    AWS --> R4["Automated Operations"]
    AWS --> R5["Incident Resolution"]

    R1 --> Final["Enterprise AI Assistant for Amazon EKS"]
    R2 --> Final
    R3 --> Final
    R4 --> Final
    R5 --> Final
```

## End Goal

**Enterprise AI Assistant**

- Build an intelligent AI assistant for Amazon EKS.
- Use **LLMs** for reasoning and natural language interaction.
- Integrate **Tool Calling** to perform Kubernetes and AWS operations.
- Use **RAG** to retrieve enterprise knowledge from internal documentation.
- Implement **AI Agents** to automate complex operational workflows.
- Evolve into a complete **AI-Ops Platform** capable of:
  - Detecting anomalies
  - Predicting failures
  - Performing root cause analysis
  - Recommending remediations
  - Executing automated operational tasks
  - Managing enterprise Kubernetes environments intelligently


# Enterprise AI Workflow for Amazon EKS

```text
                               User / SRE / DevOps Engineer
                                          │
                                          ▼
                                 Natural Language Query
                                          │
                                          ▼
                               Enterprise AI Assistant
                                          │
                                          ▼
                                   Conversation Memory
                                          │
                             ┌────────────┴────────────┐
                             │                         │
                             ▼                         ▼
                    Previous Context?            No Previous Context
                             │                         │
                             └────────────┬────────────┘
                                          ▼
                               Need Enterprise Knowledge?
                                          │
                        ┌─────────────────┴─────────────────┐
                        │                                   │
                       No                                  Yes
                        │                                   │
                        │                          Enterprise RAG
                        │                                   │
                        │                    ┌──────────────┼──────────────┐
                        │                    │              │              │
                        │                    ▼              ▼              ▼
                        │                Runbooks      GitHub Repo    Confluence
                        │                    │
                        │                    ▼
                        │               Jira / Helm
                        │                    │
                        │                    ▼
                        │            Kubernetes YAML
                        │                    │
                        └──────────────┬─────┘
                                       ▼
                            Need External Action?
                                       │
                    ┌──────────────────┴──────────────────┐
                    │                                     │
                   No                                    Yes
                    │                                     │
                    ▼                                     ▼
            Generate Answer                      Tool Selector (LLM)
                                                        │
                        ┌───────────────────────────────┼──────────────────────────────┐
                        │                               │                              │
                        ▼                               ▼                              ▼
                 Kubernetes Tool                 CloudWatch Tool                 AWS Tool
                        │                               │                              │
                        ▼                               ▼                              ▼
                 Get Pods/Logs                 Metrics/Alarms                 AWS Services
                        │                               │                              │
                        └───────────────┬───────────────┴───────────────┬──────────────┘
                                        ▼
                                Execute Operations
                                        │
                                        ▼
                                  Tool Response
                                        │
                                        ▼
                              Final LLM Reasoning
                                        │
                                        ▼
                          AI Agent / Workflow Decision
                                        │
                  ┌─────────────────────┼─────────────────────┐
                  │                     │                     │
                  ▼                     ▼                     ▼
           Detect Anomaly        Root Cause Analysis    Predict Failure
                  │                     │                     │
                  └─────────────────────┼─────────────────────┘
                                        ▼
                               Save Conversation Memory
                                        │
                                        ▼
                         Intelligent Response to the User
```

## Enterprise AI Goal

**Question → Memory → RAG → Tool Selection → Kubernetes/AWS → AI Reasoning → AI Agent → Prediction → Memory → Intelligent Response**

This architecture gradually evolves from a simple chatbot into an **Enterprise AI-Ops Platform** capable of:
- Understanding user intent
- Remembering previous conversations
- Retrieving enterprise knowledge using RAG
- Calling Kubernetes and AWS tools
- Performing intelligent reasoning with LLMs
- Detecting anomalies
- Predicting incidents before failures occur
- Executing automated operational workflows on Amazon EKS