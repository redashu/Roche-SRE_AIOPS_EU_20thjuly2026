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