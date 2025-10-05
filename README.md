# 🧠 DR. AI — Disease Information Assistant (WHO-Based)

**DR. AI** is an intelligent health assistant that provides accurate, human-like answers about major diseases such as **Cholera, Cancer, Malaria, COVID-19, and Rabies**.  
It uses official **WHO (World Health Organization)** factsheets as its verified source of truth and combines **AI-driven embeddings**, **semantic similarity search**, and **large language models (LLMs)** to generate safe, human-friendly explanations.

This project bridges the gap between authentic medical data and accessible AI-powered health insights.

---

## 🌍 Project Overview

The purpose of DR. AI is to build a **reliable, domain-specific question-answering assistant** that:
- Understands natural language queries.  
- Retrieves accurate medical information from WHO factsheets.  
- Provides clear and human-like explanations.  
- Ensures factual accuracy by relying strictly on WHO data.  

The system integrates **semantic search, local embeddings, and LLM inference** into a single application, with a user interface built using **Streamlit**.

---

## 🧩 Workflow Summary

### 1. Data Collection (Web Scraping)
Official WHO factsheets for the diseases Cholera, Cancer, Malaria, COVID-19, and Rabies were collected through web scraping.  
The scraped content was cleaned and organized into a structured dataset containing:
- Disease name  
- Heading or section title  
- Descriptive text  

---

### 2. Data Chunking
The collected text was divided into smaller, meaningful **chunks** to preserve context and improve semantic representation.  
This step enhances retrieval accuracy and model performance during similarity search.

---

### 3. Embeddings Creation
Each text chunk was converted into numerical **vector embeddings** using the **BGE-M3** model.  
These embeddings capture the semantic meaning of the text, enabling similarity comparisons between user queries and stored data.

---

### 4. Data Storage
The embeddings, along with corresponding disease data, were serialized and stored efficiently using **Joblib**.  
This allows for quick loading without regenerating embeddings every time the application runs.

---

### 5. User Query Handling
Users interact with the system via a **Streamlit interface** by entering disease-related questions such as:
- “What are the symptoms of Malaria?”  
- “How can Cholera be prevented?”  
- “What is the treatment for Cancer?”

If a user asks a question outside these topics, the model responds that it can only handle known WHO-listed diseases.

---

### 6. Query Embedding and Similarity Search
When a question is submitted:
- The query is transformed into a vector using the same embedding model.  
- The system calculates **cosine similarity** between the question vector and the dataset embeddings.  
- The top-matching chunks are retrieved as the most relevant information sources.

---

### 7. LLM Inference (Response Generation)
The retrieved text chunks are provided as context to the **LLaMA 3.2** model.  
The model then generates a natural, factual, and human-like answer based only on the retrieved WHO information.

The response is:
- Factually correct (limited to verified WHO data).  
- Written in a user-friendly and clear tone.  
- Restricted to the known disease topics.  

---

### 8. Response Display via Streamlit
The final response is displayed in the **Streamlit interface**, with a smooth workflow including:
- A title and user prompt.  
- A text input box.  
- A loading spinner during processing.  
- The final AI-generated answer.

> ⚠️ The Streamlit UI was successfully developed, but **final debugging and UI testing** are pending due to temporary hardware issues.  
> All backend processes have been verified and are functioning correctly.

---

## ⚙️ Technologies Used

**Core Technologies**
- Python  
- Streamlit  

**Data Handling and Storage**
- Pandas  
- Joblib  
- NumPy  

**Machine Learning / AI**
- BGE-M3 (for embeddings generation)  
- LLaMA 3.2 (for large language model inference)  
- scikit-learn (for cosine similarity calculation)

**Networking and Web**
- Requests (for model and API communication)  

**Data Source**
- Official WHO Factsheets  

---

## 🧠 System Architecture Overview

**Step-by-Step Flow:**
1. WHO data collected via web scraping.  
2. Text processed and divided into smaller chunks.  
3. Embeddings generated for each text segment using BGE-M3.  
4. Embeddings stored with Joblib for efficiency.  
5. User enters a question through the Streamlit interface.  
6. Question converted into an embedding vector.  
7. Cosine similarity identifies the most relevant data.  
8. Relevant information provided to LLaMA 3.2 for response generation.  
9. The system displays the AI’s answer based on verified WHO data.

---

## 💡 Features and Advantages

- Relies exclusively on **trusted WHO health information**.  
- Uses **semantic understanding** rather than simple keyword search.  
- Provides **human-readable explanations** through LLaMA 3.2.  
- Runs completely **offline** using local AI models.  
- Modular and scalable — new diseases can easily be added.  
- Promotes **safe and responsible AI** for health-related topics.

---

## 🛠️ Current Status and Future Improvements

### ✅ Current Progress
- WHO data collected and cleaned.  
- Embeddings successfully generated and stored.  
- Backend and retrieval logic fully functional.  
- Streamlit UI designed and operational.  
- Minor error fixing pending due to system hardware issues.  

### 🔮 Future Plans
- Complete user interface debugging and testing.  
- Expand coverage to include more diseases.  
- Integrate FAISS for faster vector searches.  
- Enable real-time response streaming in the UI.  
- Add a safety validation layer for medical reliability.  
- Host the app on Streamlit Cloud with private data storage.  

---

## 📦 Installation and Setup

### 1. Clone the Repository
```bash
git clone https://github.com/<your-username>/DR-AI.git
cd DR-AI
pip install streamlit joblib scikit-learn pandas numpy requests
python rag.py
