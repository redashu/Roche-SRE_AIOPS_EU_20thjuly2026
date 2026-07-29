# Understanding Vector Dimensions in Embedding Models

Different embedding models use different vector sizes depending on their architecture. Furthermore, many modern models—including Amazon Titan Text Embeddings v2—allow you to customize the dimension size depending on your needs for speed, storage cost, and accuracy.

## 1. Vector Dimension Options in Amazon Titan Embeddings v2

When you called Bedrock in your code, you explicitly asked for 1024 dimensions:

```python
body = {
    "inputText": question,
    "dimensions": 1024,  # <--- You requested 1024 here
    "normalize": True
}
```

## However, Titan Text Embeddings v2 supports three dimension choices:

| Dimensions | Description |
|------------|-------------|
| **1024** (Default) | Maximum semantic accuracy and retrieval quality |
| **512** | Retains ~99% of the accuracy of 1024 dimensions while cutting storage and memory usage in half |
| **256** | Retains ~97% of the accuracy while saving 75% on vector storage costs and speeding up search latency |

However, Titan Text Embeddings v2 supports three dimension choices:

- **1024 dimensions (Default)**: Maximum semantic accuracy and retrieval quality
- **512 dimensions**: Retains ~99% of the accuracy of 1024 dimensions while cutting storage and memory usage in half
- **256 dimensions**: Retains ~97% of the accuracy while saving 75% on vector storage costs and speeding up search latency


## 2. Common Vector Dimensions Across Industry Models

Different AI providers design their embedding models with different vector lengths:

| Provider / Model | Default Dimensions | Flexible Dimensions? |
|-----------------|-------------------|---------------------|
| Amazon Titan Text Embeddings v2 | 1024 | Yes (256, 512, 1024) |
| Amazon Titan Text Embeddings v1 | 1536 | No (Fixed) |
| OpenAI text-embedding-3-small | 1536 | Yes (Customizable down to 256) |
| OpenAI text-embedding-3-large | 3072 | Yes (Customizable) |
| Cohere Embed v3 | 1024 | Yes |
| Open-source All-MiniLM-L6-v2 | 384 | No (Fixed) |

## 3. How Vector DBs Store Embeddings

Vector databases (such as **FAISS**, **OpenSearch**, **Pinecone**, or **pgvector**) store embeddings as **contiguous arrays of floating-point numbers** along with the associated document metadata (such as document ID, source, chunk text, timestamps, or other attributes).

### Storage Format

Each embedding is represented as a fixed-length vector where every dimension is typically stored as a **32-bit floating-point value (`float32`)**, consuming:

- **4 bytes per dimension**

For example:

- **1024-dimensional vector**
  - Memory = **1024 × 4 bytes**
  - = **4,096 bytes (~4 KB)** per document chunk

- **256-dimensional vector**
  - Memory = **256 × 4 bytes**
  - = **1,024 bytes (~1 KB)** per document chunk

### Memory Example

Suppose you have **1,000,000 document chunks**.

| Embedding Size | Memory per Vector | Total Memory |
|---------------|------------------:|-------------:|
| 256D | ~1 KB | ~1 GB |
| 512D | ~2 KB | ~2 GB |
| 768D | ~3 KB | ~3 GB |
| 1024D | ~4 KB | ~4 GB |

> **Note:** These estimates account only for the raw embedding vectors. Additional memory is required for vector indexes (such as HNSW or IVF), metadata, and database overhead.

### Why Fixed Dimensions Matter

A vector database stores all vectors in a collection using a **single predefined dimensionality**. During similarity search, mathematical operations (such as cosine similarity, Euclidean distance, or dot product) require vectors to have identical lengths.

> **Critical Rule:** Every vector inserted into a specific **FAISS index** or **Vector DB collection** must have the **exact same number of dimensions**.

For example:

- ✅ 512D + 512D → Allowed
- ✅ 1024D + 1024D → Allowed
- ❌ 512D + 1024D → **Not allowed**

If you change your embedding model (for example, from a 512D model to a 1024D model), you must create a **new vector index or collection** and regenerate embeddings for all documents before performing similarity search.