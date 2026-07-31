# 📄 Intelligent Document Understanding Platform

## Overview

The Intelligent Document Understanding Platform is an AI-powered application that enables users to upload PDF documents and ask natural language questions about their content. The system extracts text from uploaded PDFs, converts it into embeddings, stores them in a FAISS vector database, retrieves the most relevant information, and uses Google Gemini to generate context-aware answers.

---

## Features

- Upload PDF documents
- Extract text from PDFs
- Display PDF metadata
  - File Name
  - File Size
  - Number of Pages
  - Character Count
- Split text into chunks
- Generate embeddings using Sentence Transformers
- Store embeddings using FAISS
- Retrieve relevant document chunks
- Answer questions using Google Gemini 3.5 Flash
- Display retrieved context for transparency
- Handle Gemini API errors gracefully

---

## Technologies Used

- Python
- Streamlit
- Google Gemini API
- Sentence Transformers
- FAISS
- PyPDF
- NumPy
- python-dotenv

---

## Project Structure

```text
DocumentAI/
│
├── app.py
├── requirements.txt
├── README.md
├── .env.example
├── uploads/
├── vectorstore/
└── utils/
    ├── pdf_loader.py
    ├── embeddings.py
    └── vector_db.py
```

## Installation

1. Clone the repository.

2. Install dependencies.

```bash
pip install -r requirements.txt
```

3. Create a `.env` file.

```
GOOGLE_API_KEY=YOUR_API_KEY
```

4. Run the application.

```bash
streamlit run app.py
```

---

## Workflow

1. Upload a PDF.
2. Extract document text.
3. Split text into chunks.
4. Generate embeddings.
5. Store embeddings in FAISS.
6. Enter a question.
7. Retrieve relevant chunks.
8. Generate an answer using Gemini.

---

## Future Enhancements

- Support DOCX and TXT files
- Multi-document search
- Chat history
- User authentication
- Cloud deployment

---

## Author

**Bhavana Sudhakar**
