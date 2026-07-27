# Roche-SRE_AIOPS_EU_20thjuly2026

### Revision 

<img src="rev1.png">

## model para in LLM 

<img src="llm1.png">

### checking tool directories

```
[ec2-user@ip-172-31-27-32 ~]$ ls
ashu-roche-codes  ashu-roche-env
[ec2-user@ip-172-31-27-32 ~]$ source ashu-roche-env/bin/activate
(ashu-roche-env) [ec2-user@ip-172-31-27-32 ~]$ ls
ashu-roche-codes  ashu-roche-env
(ashu-roche-env) [ec2-user@ip-172-31-27-32 ~]$ cd ashu-roche-codes/
(ashu-roche-env) [ec2-user@ip-172-31-27-32 ashu-roche-codes]$ ls
Roche-SRE_AIOPS_EU_20thjuly2026  bedrock-converse.py    llm_chat.py         nova-chat.py   test-aws-bedrock.py
ashu-ui-app                      invoke.py              model_inference.py  nova_model.py
bedrock-converse-mem.py          llm-copilot-roche-app  my-chat-app         roche-webapp
(ashu-roche-env) [ec2-user@ip-172-31-27-32 ashu-roche-codes]$ ls llm-copilot-roche-app/
start-calling.py  tool_calling_summarizer.py.py  tools
(ashu-roche-env) [ec2-user@ip-172-31-27-32 ashu-roche-codes]$ 

```

## testing response summary 

```
(ashu-roche-env) [ec2-user@ip-172-31-27-32 llm-copilot-roche-app]$ ls
response_summary.py  start-calling.py  tool_calling_summarizer.py.py  tools
(ashu-roche-env) [ec2-user@ip-172-31-27-32 llm-copilot-roche-app]$ 
(ashu-roche-env) [ec2-user@ip-172-31-27-32 llm-copilot-roche-app]$ 
(ashu-roche-env) [ec2-user@ip-172-31-27-32 llm-copilot-roche-app]$ python3 response_summary.py 

Kubernetes AI Assistant
Type 'exit' to quit.

Ask : shoe me running pods 

LLM Seletected Tool Response : get_all_pods

Selected Tool : get_all_pods

Generating Response...

================================================================================

```
### more tools to get project going 

```
(ashu-roche-env) [ec2-user@ip-172-31-27-32 llm-copilot-roche-app]$ touch  tools/describe_pods.py 
(ashu-roche-env) [ec2-user@ip-172-31-27-32 llm-copilot-roche-app]$ touch  tools/get_cluster_events.py 
(ashu-roche-env) [ec2-user@ip-172-31-27-32 llm-copilot-roche-app]$ touch  tools/get_pod_logs.py 
(ashu-roche-env) [ec2-user@ip-172-31-27-32 llm-copilot-roche-app]$ touch  tools/get_pod_resource_usage.py 
(ashu-roche-env) [ec2-user@ip-172-31-27-32 llm-copilot-roche-app]$ touch  tools/get_unhealthy_pods.py 
(ashu-roche-env) [ec2-user@ip-172-31-27-32 llm-copilot-roche-app]$ touch  tools/get_unhealthy_pods.py 
(ashu-roche-env) [ec2-user@ip-172-31-27-32 llm-copilot-roche-app]$ tree tools
tools
├── __pycache__
│   ├── all_pods.cpython-313.pyc
│   └── tool_selector.cpython-313.pyc
├── all_deployments.py
├── all_nodes.py
├── all_pods.py
├── all_services.py
├── describe_pods.py
├── get_cluster_events.py
├── get_pod_logs.py
├── get_pod_resource_usage.py
├── get_unhealthy_pods.py
├── tool_registry.py
└── tool_selector.py

```
