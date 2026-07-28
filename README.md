#  Semantic Search using Sentence Transformers

This project demonstrates how to generate semantic text embeddings using the `sentence-transformers` library and compare the similarity between two sentences.

Instead of matching words exactly, semantic search understands the meaning of text by converting sentences into high-dimensional vector embeddings. These embeddings can then be compared to determine how semantically similar two sentences are.

---

##  Features

- Generate sentence embeddings using a pre-trained transformer model.
- Compare the semantic similarity between two sentences.
- Simple and beginner-friendly implementation.
- Built with Python and NumPy.
- Uses the lightweight `all-MiniLM-L6-v2` embedding model.

---

##  Technologies Used

- Python
- Sentence Transformers
- NumPy
- Hugging Face Transformers

---

##  Project Structure

```
semantic_Search.py
README.md
```

---

##  Installation

Clone the repository:

```bash
git clone https://github.com/GokulBits18/your-repository.git
cd your-repository
```

Install the required libraries:

```bash
pip install sentence-transformers numpy
```

---

##  Run the Project

```bash
python semantic_Search.py
```

---

##  Example Code

```python
from sentence_transformers import SentenceTransformer
import numpy as np

sentences = [
    "i like bike",
    "i like bike color" # ---- ( you can try with other sentences also ) -----
]

model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)

embeddings = model.encode(sentences)

similarity = np.dot(
    embeddings[0],
    embeddings[1]
)

print(f"{similarity * 100:.2f}% similar")
```

---

##  Example Output

```
89.54% similar
```

(The exact value may vary slightly depending on the model version.)

---

##  How It Works

1. Load a pre-trained Sentence Transformer model.
2. Convert each sentence into a dense numerical vector (embedding).
3. Compute the similarity between the embeddings.
4. Display the similarity score.

---

##  What are Embeddings?

Embeddings are numerical vector representations of data such as text, images, or audio. They capture semantic meaning, allowing computers to understand relationships between different pieces of information.

For example:

```
"I like bikes"
"I love motorcycles"
```

Although these sentences use different words, their embeddings are close because they express similar meanings.

---

##  Applications

- Semantic Search
- AI Chatbots
- Document Retrieval
- Recommendation Systems
- Question Answering
- Duplicate Text Detection
- Information Retrieval
- Natural Language Processing (NLP)

---

##  Model Used

**all-MiniLM-L6-v2**

- Lightweight transformer model
- Fast inference
- Produces 384-dimensional sentence embeddings
- Optimized for semantic similarity and retrieval tasks

---

##  pic 

<img width="1468" height="67" alt="image" src="https://github.com/user-attachments/assets/1af7df91-8d40-4bd7-9158-e1f2979f531e" />
<img width="1466" height="52" alt="image" src="https://github.com/user-attachments/assets/4a0daad6-1171-4d3b-813b-29252e48bbaa" />
<img width="1461" height="56" alt="image" src="https://github.com/user-attachments/assets/ac521ac6-38bb-4030-b7d9-54c84bf7822f" />

## just trying with other sentences 

<img width="1471" height="201" alt="image" src="https://github.com/user-attachments/assets/747bd08f-9e9f-4c3b-ac47-df08c97307d0" />


