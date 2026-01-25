# 🧠 Laboratory Work No. 3  
**Course:** Neural Network Technologies and Systems  
**Topic:** Implementation of a RAG System for Knowledge Extraction  
**Variant:** No. 2 — Chroma + TXT + Local LLM  

---

## 🎯 Purpose
To gain practical skills in building a **Retrieval-Augmented Generation (RAG)** system  
that combines **vector search** with a **large language model** to generate answers  
based on external knowledge sources.

---

## ⚙️ Implementation

### 🧩 Main stages:
1. **Corpus preparation**
   - 5 `.txt` files on quantum physics topics.
   - Loaded via `DirectoryLoader`.

2. **Text splitting**
   - Used `RecursiveCharacterTextSplitter`
   - `chunk_size=300`, `chunk_overlap=50`

3. **Vectorization**
   - Model: `sentence-transformers/all-MiniLM-L6-v2`

4. **Vector database**
   - Storage: **Chroma**
   - Saved to disk (`persist_directory`)

5. **Retriever**
   - Modes: `similarity` and `mmr`
   - Metadata filtering supported

6. **RAG chain**
   - Retriever → Prompt → LLM → Output
   - Connected to a local LLM via **OpenAI-compatible API** (NGROK)

---

## 📁 Project structure
```
project/
│
├── data/quantum_computer_n
├── chroma_db/
├── RAG.ipynb
└── README.md
```

---

## 🧠 Main files

### `RAG.ipynb`
Contains:
- document loading,
- text splitting,
- vector DB creation,
- retrievers,
- RAG chain.

---

## 🔍 Search mode comparison

| Mode | Feature | Result |
|--------|-------------|------------|
| similarity | maximum relevance | more focused context |
| mmr | balance of relevance and diversity | more diverse answers |

---

## 📈 Results
- Correct text indexing.
- Successful semantic search.
- Context-aware answer generation.
- Metadata filtering support.

---

## 💬 Conclusions
A full RAG system with **Chroma** vector store and a local LLM was implemented.  
The **MMR** mode provided more diverse answers,  
while metadata filtering improved search accuracy.

---

## 👩‍💻 Author
**Olijnyk Sofiia**  
Group OI-45  
Specialty 122 — Computer Science  
Lviv Polytechnic National University
