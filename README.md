# 🧠 AI Research Paper Intelligence Platform

An AI-powered system that analyzes research papers and allows users to ask questions using **Retrieval-Augmented Generation (RAG)**.

---

## 📸 Application Preview

<img width="1890" height="755" alt="image" src="https://github.com/user-attachments/assets/47fde3c6-31d6-4334-8941-f3709d6a18a3" />

<img width="1857" height="642" alt="image" src="https://github.com/user-attachments/assets/2954ef07-7cd2-47b3-87d5-ccc5b52e2013" />

<img width="1837" height="586" alt="image" src="https://github.com/user-attachments/assets/7cb285d9-bf0a-483c-9976-17831b199eac" />




## 🚀 Features

*  Upload one or multiple research papers (PDF)
*  Automatic text cleaning and preprocessing
*  Intelligent document chunking
*  Semantic search using **FAISS**
*  RAG-based chatbot for answering questions
*  AI-generated research summaries
*  Answers grounded with **source paragraphs from papers**
*  Interactive UI built with **Streamlit**

---

## 🧠 How It Works

```
PDF Upload
   ↓
PDF Parsing (PyMuPDF)
   ↓
Text Cleaning & Chunking
   ↓
Embeddings (Sentence Transformers)
   ↓
FAISS Vector Database
   ↓
Semantic Retrieval
   ↓
LLM (FLAN-T5)
   ↓
Answer + Source Context
```

---

## 🛠️ Tech Stack

* **Python**
* **Streamlit**
* **FAISS** (Vector Database)
* **Sentence Transformers** (Embeddings)
* **HuggingFace Transformers** (LLM)
* **PyMuPDF** (PDF Parsing)

---

## 💬 Example Questions

You can ask:

* What dataset was used?
* What problem does the paper address?
* What method is proposed?
* What results were achieved?

---

## 📦 Installation

Clone the repository:

```bash
# 🧠 AI Research Paper Intelligence Platform

An AI-powered system that analyzes research papers and allows users to ask questions using **Retrieval-Augmented Generation (RAG)**.

---

## 🚀 Features

*  Upload one or multiple research papers (PDF)
*  Automatic text cleaning and preprocessing
*  Intelligent document chunking
*  Semantic search using FAISS
*  RAG-based chatbot for answering questions
*  AI-generated research summaries
*  Answers grounded with source paragraphs from papers
*  Interactive UI built with Streamlit

---

## 🧠 How It Works

```
PDF Upload
   ↓
PDF Parsing (PyMuPDF)
   ↓
Text Cleaning & Chunking
   ↓
Embeddings (Sentence Transformers)
   ↓
FAISS Vector Database
   ↓
Semantic Retrieval
   ↓
LLM (FLAN-T5)
   ↓
Answer + Source Context
```

---

## 🛠️ Tech Stack

* **Python**
* **Streamlit**
* **FAISS** (Vector Database)
* **Sentence Transformers** (Embeddings)
* **HuggingFace Transformers** (LLM)
* **PyMuPDF** (PDF Parsing)

---

## 💬 Example Questions

You can ask:

* What dataset was used?
* What problem does the paper address?
* What method is proposed?
* What results were achieved?

---

## 📦 Installation

Clone the repository:

```bash
https://github.com/FatamaOkasha/Ai-research-paper-intelligence.git
cd ai-research-paper-intelligence
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the App

```bash
streamlit run frontend/dashboard.py
```

---

## 📁 Project Structure

```
backend/
│
├── parser/            # PDF parsing
├── preprocessing/     # cleaning & chunking
├── embeddings/        # embedding model
├── database/          # FAISS vector store
├── summarization/     # paper summarization
├── rag/               # chatbot (RAG)
└── services/          # pipeline orchestration

frontend/
└── dashboard.py       # Streamlit UI

data/                  # stored data
```

---

## 🎯 Key Highlights

* Built a **Retrieval-Augmented Generation (RAG)** system from scratch
* Supports **multi-document knowledge base**
* Improves answer reliability with **source grounding**
* Designed modular and scalable backend architecture

---

## 📌 Future Improvements

* Multi-paper comparison
* Citation graph visualization
* Literature review generation
* Advanced reranking for retrieval

---

## 👩‍💻 Author

**Fatama Okasha**

---

## ⭐ If you like this project

Give it a star ⭐ on GitHub!

cd ai-research-paper-intelligence
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the App

```bash
streamlit run frontend/dashboard.py
```

---

## 📁 Project Structure

```
backend/
│
├── parser/            # PDF parsing
├── preprocessing/     # cleaning & chunking
├── embeddings/        # embedding model
├── database/          # FAISS vector store
├── summarization/     # paper summarization
├── rag/               # chatbot (RAG)
└── services/          # pipeline orchestration

frontend/
└── dashboard.py       # Streamlit UI

data/                  # stored data
```

---

## 🎯 Key Highlights

* Built a **Retrieval-Augmented Generation (RAG)** system from scratch
* Supports **multi-document knowledge base**
* Improves answer reliability with **source grounding**
* Designed modular and scalable backend architecture

---

## 📌 Future Improvements

* Multi-paper comparison
* Citation graph visualization
* Literature review generation
* Advanced reranking for retrieval

---

## 👩‍💻 Author

**Fatama Okasha**

---

## ⭐ If you like this project

Give it a star ⭐ on GitHub!




