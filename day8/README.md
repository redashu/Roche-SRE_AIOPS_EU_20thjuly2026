# Roche-SRE_AIOPS_EU_20thjuly2026

### Revision 

<img src="rev1.png">


### RAG process understanding 

<img src="rag1.png">


### using bedrock agent runtime api engine 

<img src="rag2.png">


```
(ashu-roche-env) [ec2-user@ip-172-31-27-32 ashu-roche-codes]$ ls
RAG                              ashu-ui-app              llm-copilot-roche-app  nova-chat.py          test-aws-bedrock.py
Roche-SRE_AIOPS_EU_20thjuly2026  bedrock-converse-mem.py  llm_chat.py            nova_model.py
ashu-converse-mem-gaurdr.py      bedrock-converse.py      model_inference.py     project-orchestrator
ashu-converse-mem-summary.py     invoke.py                my-chat-app            roche-webapp
(ashu-roche-env) [ec2-user@ip-172-31-27-32 ashu-roche-codes]$ cd project-orchestrator/
(ashu-roche-env) [ec2-user@ip-172-31-27-32 project-orchestrator]$ ls
ai  investigator
(ashu-roche-env) [ec2-user@ip-172-31-27-32 project-orchestrator]$ ls  investigator/
__init__.py  executor.py  orchestrator.py  planner.py  planner_prompt.py  reducer.py
(ashu-roche-env) [ec2-user@ip-172-31-27-32 project-orchestrator]$ ls ai/
final_response_summary.py  tools
(ashu-roche-env) [ec2-user@ip-172-31-27-32 project-orchestrator]$ python3  ai/final_response_summary.py 

Kubernetes AI Assistant
Type 'exit' to quit.

Ask : tell me if any of my app is not healthy 

LLM Response : get_unhealthy_pods

Selected Tool : get_unhealthy_pods


```