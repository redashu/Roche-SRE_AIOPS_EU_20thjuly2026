# Roche-SRE_AIOPS_EU_20thjuly2026

### Understanding LLM Release and Build processing 

<img src="llm1.png">

### Access model options 

<img src="llm2.png">

### LLM concept to remember 

<img src="llm3.png">

## Login to LInux jump server using cli 

```
ssh  carlos@63.186.54.64 
** WARNING: connection is not using a post-quantum key exchange algorithm.
** This session may be vulnerable to "store now, decrypt later" attacks.
** The server may need to be upgraded. See https://openssh.com/pq.html
carlos@63.186.54.64's password: 
   ,     #_
   ~\_  ####_        Amazon Linux 2023
  ~~  \_#####\
  ~~     \###|
  ~~       \#/ ___   https://aws.amazon.com/linux/amazon-linux-2023
   ~~       V~' '->
    ~~~         /
      ~~._.   _/
         _/ _/
       _/m/'
[carlos@ip-172-31-27-32 ~]$ 
[carlos@ip-172-31-27-32 ~]$ 
[carlos@ip-172-31-27-32 ~]$ whoami
carlos

```
### Creating virtual env and installing numpy as sample lib 

```
[ec2-user@ip-172-31-27-32 ~]$ python3 -V
Python 3.13.14
[ec2-user@ip-172-31-27-32 ~]$ python3 -m  venv  ashu-roche-env
[ec2-user@ip-172-31-27-32 ~]$ ls
ashu-roche-env
[ec2-user@ip-172-31-27-32 ~]$ source  ashu-roche-env/bin/activate
(ashu-roche-env) [ec2-user@ip-172-31-27-32 ~]$ 
(ashu-roche-env) [ec2-user@ip-172-31-27-32 ~]$ 
(ashu-roche-env) [ec2-user@ip-172-31-27-32 ~]$ pip3 list
Package Version
------- -------
pip     24.2
(ashu-roche-env) [ec2-user@ip-172-31-27-32 ~]$ pip list
Package Version
------- -------
pip     24.2
(ashu-roche-env) [ec2-user@ip-172-31-27-32 ~]$ pip install numpy 
Collecting numpy
  Downloading numpy-2.5.1-cp313-cp313-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl.metadata (6.6 kB)
Downloading numpy-2.5.1-cp313-cp313-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl (16.7 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 16.7/16.7 MB 102.7 MB/s eta 0:00:00
Installing collected packages: numpy
Successfully installed numpy-2.5.1

[notice] A new release of pip is available: 24.2 -> 26.1.2
[notice] To update, run: pip install --upgrade pip
(ashu-roche-env) [ec2-user@ip-172-31-27-32 ~]$ pip list
Package Version
------- -------
numpy   2.5.1
pip     24.2

```