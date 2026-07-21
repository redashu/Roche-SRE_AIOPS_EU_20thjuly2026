import boto3

# connecting to bedrock aws service using boto3

client = boto3.client("bedrock") 
# conneting to bedrock foundation model layer 
for i in dir(client):
    if "list" in i:
        print(i)
# printing listing foundation model 
models=client.list_foundation_models()
print(models)