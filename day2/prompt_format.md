# Prompt Formats

## 1. Meta Llama Native Prompt Format

This is what you typically use in Bedrock for Llama Instruct models.

```text
<|begin_of_text|>

<|start_header_id|>system<|end_header_id|>

You are a helpful AI assistant.

<|eot_id|>

<|start_header_id|>user<|end_header_id|>

Explain Kubernetes.

<|eot_id|>

<|start_header_id|>assistant<|end_header_id|>
```

Python example:

```python
prompt = f"""
<|begin_of_text|><|start_header_id|>system<|end_header_id|>

You are a helpful AI assistant.

<|eot_id|>

<|start_header_id|>user<|end_header_id|>

Explain Kubernetes.

<|eot_id|>

<|start_header_id|>assistant<|end_header_id|>
"""
```

This is the official prompt format for Llama Instruct models when using the native inference API.

## 2. OpenAI GPT

OpenAI does not use prompt tokens. Instead, it uses structured messages.

```python
messages = [
    {
        "role": "system",
        "content": "You are a helpful AI assistant."
    },
    {
        "role": "user",
        "content": "Explain Kubernetes."
    }
]
```

Conversation example:

```python
messages = [
    {
        "role": "system",
        "content": "You are an SRE expert."
    },
    {
        "role": "user",
        "content": "Explain CrashLoopBackOff."
    },
    {
        "role": "assistant",
        "content": "CrashLoopBackOff occurs..."
    },
    {
        "role": "user",
        "content": "How do I fix it?"
    }
]
```

Notice:

- Everything is a message.

## 3. Anthropic Claude

Claude is also message based.

Example:

```python
system = "You are a Kubernetes expert."

messages = [
    {
        "role": "user",
        "content": [
            {
                "type": "text",
                "text": "Explain Kubernetes."
            }
        ]
    }
]
```

Claude separates the system prompt from the conversation messages, unlike Llama's native prompt string.