# 📄 Intelligent Document Understanding Platform

An AI-powered document question-answering application that allows users to upload PDF documents and ask natural language questions about their content. The platform extracts text, generates embeddings, stores them in a FAISS vector database, retrieves the most relevant context, and uses Google Gemini to provide accurate answers.

---

## ✨ Features

- 📄 Upload PDF documents
- 📝 Extract text from PDFs
- 📊 Display PDF metadata
  - File Name
  - File Size
  - Number of Pages
  - Character Count
- ✂️ Split text into chunks
- 🧠 Generate embeddings using Sentence Transformers
- 🗂️ Store embeddings using FAISS
- 🔍 Retrieve relevant document chunks
- 🤖 Generate answers using Google Gemini
- 📌 Display retrieved context for transparency
- ⚠️ Gracefully handle Gemini API errors

---

## 🛠️ Technologies Used

- Python
- Streamlit
- Google Gemini API
- Sentence Transformers
- FAISS
- PyPDF
- NumPy
- python-dotenv

---

## 📁 Project Structure

```text
Intelligent-Document-Understanding-Platform/
│
├── app.py
├── requirements.txt
├── README.md
├── .env.example
├── uploads/
│   └── .gitkeep
└── utils/
    ├── pdf_loader.py
    ├── embeddings.py
    └── vector_db.py
```

---

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/bhavanasudhakar29/Intelligent-Document-Understanding-Platform.git
```

### 2. Navigate to the project

```bash
cd Intelligent-Document-Understanding-Platform
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Create a `.env` file

```env
GOOGLE_API_KEY=YOUR_API_KEY
```

### 5. Run the application

```bash
streamlit run app.py
```

---

## 🔄 Workflow

1. Upload a PDF document.
2. Extract text from the document.
3. Split the text into chunks.
4. Generate embeddings using Sentence Transformers.
5. Store embeddings in a FAISS vector database.
6. Ask a question about the document.
7. Retrieve the most relevant document chunks.
8. Generate an AI-powered answer using Google Gemini.

---

## 🚀 Future Enhancements

- Support DOCX and TXT files
- Multi-document search
- Chat history
- User authentication
- Cloud deployment

---

## 👩‍💻 Author

**Bhavana Sudhakar**

GitHub: https://github.com/bhavanasudhakar29
