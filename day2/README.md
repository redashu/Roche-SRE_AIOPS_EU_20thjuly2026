# Roche-SRE_AIOPS_EU_20thjuly2026

### basic command to check with 

```
ec2-user@ip-172-31-27-32 ~]$ who
pallavi  pts/0        2026-07-21 09:35 (195.133.129.178)
ec2-user pts/4        2026-07-21 10:19 (196.3.49.254)
tuach    pts/8        2026-07-21 10:20 (86.175.234.66)
raul     pts/9        2026-07-21 10:20 (79.116.137.82)
marc     pts/12       2026-07-21 10:20 (86.127.224.22)
emmanuel pts/10       2026-07-21 10:21 (46.205.205.10)
[ec2-user@ip-172-31-27-32 ~]$ 
[ec2-user@ip-172-31-27-32 ~]$ cat ~/.config/code-server/config.yaml 
bind-addr: 0.0.0.0:8080
auth: password
password: 345436546dfgdgdfgfdgf
cert: false
[ec2-user@ip-172-31-27-32 ~]$ ls
ashu-roche-codes  ashu-roche-env
[ec2-user@ip-172-31-27-32 ~]$ source  ashu-roche-env/bin/activate
(ashu-roche-env) [ec2-user@ip-172-31-27-32 ~]$ pip3 list
Package         Version
--------------- -----------
boto3           1.43.51
botocore        1.43.51
jmespath        1.1.0
numpy           2.5.1
pip             24.2
python-dateutil 2.9.0.post0
s3transfer      0.19.1
six             1.17.0


```

### connecting to any aws service with auth / login using boto3

```
(ashu-roche-env) [ec2-user@ip-172-31-27-32 ~]$ python3
Python 3.13.14 (main, Jun 16 2026, 00:00:00) [GCC 11.5.0 20240719 (Red Hat 11.5.0-5)] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import boto3
>>> dir(boto3)
['DEFAULT_SESSION', 'NullHandler', 'Session', '__author__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', '__version__', '_get_default_session', '_warn_deprecated_python', 'client', 'compat', 'docs', 'exceptions', 'logging', 'resource', 'resources', 'session', 'set_stream_logger', 'setup_default_session', 'utils']
>>> 
>>> x1=boto3.client("ec2")
>>> aws_bedrock=boto3.client("bedrock")
>>> 


```

### aws cli to check bedrock foundation model layer 

```
62  aws bedrock   list-foundation-models
   63  aws bedrock   list-foundation-models --output table 
   64  aws bedrock   list-foundation-models --output table   --query "modelSummaries[].modelId"
   65  aws bedrock   list-foundation-models --output table   --query "modelSummaries[*].[modelId,modelName,providerName]"
   66  aws bedrock   list-foundation-models --output table   --query "modelSummaries[*].[modelId,modelName,providerName]"  --by-provider Meta

```

### python manual coding 

```

python3
Python 3.13.14 (main, Jun 16 2026, 00:00:00) [GCC 11.5.0 20240719 (Red Hat 11.5.0-5)] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import boto3
>>> aws_bedrock=boto3.client("bedrock")
>>> for i in dir(aws_bedrock):
...     if "list" in i:
...         print(i)
...         
list_advanced_prompt_optimization_jobs
list_automated_reasoning_policies
list_automated_reasoning_policy_build_workflows
list_automated_reasoning_policy_test_cases
list_automated_reasoning_policy_test_results
list_custom_model_deployments
list_custom_models
list_enforced_guardrails_configuration
list_evaluation_jobs
list_foundation_model_agreement_offers
list_foundation_models
list_guardrails
list_imported_models
list_inference_profiles
list_marketplace_model_endpoints
list_model_copy_jobs
list_model_customization_jobs
list_model_import_jobs
list_model_invocation_jobs
list_prompt_routers
list_provisioned_model_throughputs
list_tags_for_resource
>>> models=aws_bedrock.list_foundation_models()

```

## for Model interacting we need to have some details 

<img src="ml2.png">

