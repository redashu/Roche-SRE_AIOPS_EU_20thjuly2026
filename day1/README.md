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

### to get vscode password of your own user 

```
 cat   ~/.config/code-server/config.yaml 
bind-addr: 0.0.0.0:8080
auth: password

```

### python boto3 the aws SDK module 

```
(ashu-roche-env) [ec2-user@ip-172-31-27-32 ashu-roche-codes]$ pip3 install boto3


===>
ashu-roche-env) [ec2-user@ip-172-31-27-32 ashu-roche-codes]$ pip3 list
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
urllib3         2.7.0
(ashu-roche-env) [ec2-user@ip-172-31-27-32 ashu-roche-codes]$ python
Python 3.13.14 (main, Jun 16 2026, 00:00:00) [GCC 11.5.0 20240719 (Red Hat 11.5.0-5)] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 
>>> import boto3
>>> dir(boto3)
['DEFAULT_SESSION', 'NullHandler', 'Session', '__author__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', '__version__', '_get_default_session', '_warn_deprecated_python', 'client', 'compat', 'docs', 'exceptions', 'logging', 'resource', 'resources', 'session', 'set_stream_logger', 'setup_default_session', 'utils']
>>> exit;
Use exit() or Ctrl-D (i.e. EOF) to exit
>>> 
```
