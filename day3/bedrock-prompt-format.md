# Amazon Bedrock Converse API Prompt Example

This example shows how to call the Converse API with:

- A system instruction
- A user message
- Inference configuration (`temperature`, `topP`, `maxTokens`)

```python
response = client.converse(
    modelId=MODEL_ID,
    system=[
        {
            "text": "You are an experienced Site Reliability Engineer."
        }
    ],
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "text": "Explain CrashLoopBackOff."
                }
            ]
        }
    ],
    inferenceConfig={
        "temperature": 0,
        "topP": 0.9,
        "maxTokens": 512
    }
)
```