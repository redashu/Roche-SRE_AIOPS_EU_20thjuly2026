import boto3

# connecting to bedrock aws service using boto3

client = boto3.client("bedrock") 
# conneting to bedrock foundation model layer 
for i in dir(client):
    if "list" in i:
        print(i)
# printing listing foundation model 
models=client.list_foundation_models(
    byProvider="Anthropic"
)
print(models["modelSummaries"])
# complete this -- print all antropic related -- Modelid , name , input , output Modalities

for i in models["modelSummaries"]:
    print(f" Model ID   :  {i['modelId']}")
    print(f" Model Name   :  {i['modelName']}")