# Roche-SRE_AIOPS_EU_20thjuly2026

## chat app flask directory structure 

```
tree  ashu-ui-app/
ashu-ui-app/
├── app.py
├── requirements.txt
└── templates
    └── index.html


```

### Installing python modules using file 

```
 pip3 install -r requirements.txt 
```

### LLM copilot app with tools 

<img src="tool1.png">

### checking aws / eks / kubectl related details

```
(ashu-roche-env) [ec2-user@ip-172-31-27-32 ~]$ aws  s3  ls
2026-04-27 13:28:42 ashutoshh-tf-test-bucket
2026-05-26 04:18:17 cf-templates-p5tewb2jg6i-ap-south-1
2026-04-22 03:17:02 delvex-software-center
2026-06-25 04:35:10 demobucketdatahub
(ashu-roche-env) [ec2-user@ip-172-31-27-32 ~]$ eksctl  get cluster --region us-east-1
NAME		REGION		EKSCTL CREATED
my-cluster	us-east-1	True
(ashu-roche-env) [ec2-user@ip-172-31-27-32 ~]$ 
(ashu-roche-env) [ec2-user@ip-172-31-27-32 ~]$ 
(ashu-roche-env) [ec2-user@ip-172-31-27-32 ~]$ kubectl version --client 
Client Version: v1.34.6-eks-bbe087e
Kustomize Version: v5.7.1
(ashu-roche-env) [ec2-user@ip-172-31-27-32 ~]$ 

===>


 aws eks update-kubeconfig --name my-cluster --region us-east-1
Added new context arn:aws:eks:us-east-1:992382386705:cluster/my-cluster to /home/ec2-user/.kube/config
(ashu-roche-env) [ec2-user@ip-172-31-27-32 ~]$ 
(ashu-roche-env) [ec2-user@ip-172-31-27-32 ~]$ 
(ashu-roche-env) [ec2-user@ip-172-31-27-32 ~]$ 
(ashu-roche-env) [ec2-user@ip-172-31-27-32 ~]$ kubectl  get nodes
NAME                             STATUS   ROLES    AGE    VERSION
ip-192-168-16-10.ec2.internal    Ready    <none>   2d9h   v1.34.9-eks-8f14419
ip-192-168-18-127.ec2.internal   Ready    <none>   2d9h   v1.34.9-eks-8f14419
ip-192-168-54-163.ec2.internal   Ready    <none>   2d9h   v1.34.9-eks-8f14419
(ashu-roche-env) [ec2-user@ip-172-31-27-32 ~]$ 


```
