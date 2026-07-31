# Ollama Quick Reference

## 📥 Installation & Service

| Action | Command / Method |
|--------|------------------|
| Install (macOS/Linux) | `curl -fsSL https://ollama.com/install.sh \| sh` |
| Install (Windows) | Download from https://ollama.com |
| Start Service | `ollama serve` |

## 📦 Model Management

| Action | Command | Example |
|--------|---------|---------|
| Download & Run | `ollama run <model>` | `ollama run llama3.2:1b` |
| Download Only | `ollama pull <model>` | `ollama pull gemma3:270m` |
| List Models | `ollama list` | Shows installed models |
| Delete Model | `ollama rm <model>` | `ollama rm smollm:135m` |
| Update Model | `ollama pull <model>` | Downloads latest version |
| Show Details | `ollama show <model>` | `ollama show llama3.1` |

## 💬 Chat Commands

After starting a model:

```bash
ollama run llama3.2:1b
```

| Command | Description |
|---------|-------------|
| `/exit` or `Ctrl + D` | Exit chat |
| `"""` | Multiline input |
| `/set system <prompt>` | Set system prompt |
| `/show system` | Show current system prompt |
| `/clear` | Clear conversation |
| `/?` or `/help` | Display help |

## ⚡ Quick Examples

### Ask a Question

```bash
ollama run gemma3:270m "What is the capital of France?"
```

### Review Code

```bash
cat code.py | ollama run llama3.2:1b "Find bugs in this code"
```

### Save Output

```bash
ollama run llama3.2:1b "Write a README for a Python app" > README.md
```

## ⚙️ Monitoring

```bash
ollama ps
```

> **Note:** The following content is formatted in **GitHub Flavored Markdown (GFM)** and is ready to paste directly into a `README.md` file.

# ⚖️ The Lightest Ollama Models Compared

| Model | Parameters | Download Size | Recommended RAM | Run Command |
| :---- | ---------: | ------------: | --------------: | :---------- |
| **SmolLM (135M)** | 135 Million | ~90 MB | < 500 MB | `ollama run smollm:135m` |
| **Gemma 3 (270M)** | 270 Million | ~190 MB | < 1 GB | `ollama run gemma3:270m` |
| **SmolLM (360M)** | 360 Million | ~240 MB | < 1 GB | `ollama run smollm:360m` |
| **Qwen2.5 (0.5B)** | 500 Million | ~390 MB | ~1 GB | `ollama run qwen2.5:0.5b` |
| **Llama 3.2 (1B)** | 1 Billion | ~1.3 GB | ~2 GB | `ollama run llama3.2:1b` |

## 📊 Quick Recommendations

| Use Case | Recommended Model |
| :------- | :---------------- |
| 💾 Lowest memory usage | **SmolLM (135M)** |
| ⚡ Fastest startup | **SmolLM (135M)** |
| 🖥️ Best for older PCs | **Gemma 3 (270M)** |
| ⚖️ Best balance of speed and quality | **Qwen2.5 (0.5B)** |
| 🧠 Best overall lightweight model | **Llama 3.2 (1B)** |