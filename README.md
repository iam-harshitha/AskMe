# 📚 AskMe 

An intelligent research assistant that extracts, summarizes, and finds relevant research papers based on either an uploaded research paper or a keyword/topic search.  

## 🚀 Features  

✅ Upload a Research Paper (PDF) and get a detailed summary.  
✅ Extract full text from the PDF before summarization.  
✅ Find related research papers that match the uploaded paper’s content.  
✅ Search by keyword or research topic to fetch highly relevant papers.  
✅ Interactive UI powered by Streamlit.  

---

## 📜 How It Works?  

### 🔄 Option 1: Upload a Research Paper  
1. Upload a PDF of a research paper.  
2. The system extracts the full content from the PDF.  
3. A detailed and longer summary is generated.  
4. The system fetches highly relevant research papers related to the uploaded paper.  

### 🔎 Option 2: Search by Keyword  
1. Enter a keyword or research topic.  
2. The system searches arXiv and retrieves only the most relevant research papers.  
3. The file upload section is automatically hidden when using this mode.  

---

## 🏗️ How I Built This Project  

This project was designed to assist **researchers, students, and professionals** in quickly accessing relevant research papers. Here’s how I built it:  

### 📂 **1. Data Extraction & Text Processing**  
- Used **pdfplumber** to extract text from research papers in PDF format.  
- Ensured **entire content** is read before summarization.  

### 📝 **2. Text Summarization**  
- Implemented **Hugging Face’s Transformers library** to generate a **concise and informative summary**.    

### 🔍 **3. Finding Related Papers on arXiv**  
- Used **requests** to interact with the **arXiv API**.  
- Applied **intelligent query matching** to ensure **highly relevant** papers are retrieved (not random ones).  

### 🖥️ **4. Building the Web Application**  
- Developed a **Streamlit-based interactive UI** to allow easy use.  
- Implemented **conditional UI rendering** (hiding one input section when the other is active).  
- Used **Markdown formatting in Streamlit** to present fetched research papers in a **readable** format.  

### 🚀 **5. Deployment (Optional for Future)**  
- The project is **currently running locally**, but it can be deployed on **Streamlit Sharing, AWS, or Hugging Face Spaces**.  

---

## 🛠️ Tech Stack  

| **Technology**    | **Usage** |
|------------------|------------------------------------------------|
| **Python**       | Core programming language |
| **Streamlit**    | Web framework for building the interactive UI |
| **pdfplumber**   | Extracting text from PDF research papers |
| **Transformers (Hugging Face)** | NLP model for research paper summarization |
| **Requests**     | Fetching research papers from arXiv API |

---



## 📷 Screenshots  

Here’s how the **AskMe** looks in action:  

## **Upload Research Paper Mode:** 
![Screenshot 2025-03-31 160712](https://github.com/user-attachments/assets/b8bdd1e5-8f4f-4538-867b-a5f25af62ab8)

## **Keyword Search Mode:**  
![Screenshot 2025-03-31 160353](https://github.com/user-attachments/assets/6698ebc0-6c22-4ab9-a954-580efd77b9c9)

