# 📄 Intelligent Document Understanding Platform

🚀 **Live Demo:** https://intelligent-document-understanding-platform-eettqdhowlcigetke4.streamlit.app/

An AI-powered Document Question Answering application built using **Streamlit**, **Google Gemini**, **Sentence Transformers**, and **FAISS**. The platform allows users to upload PDF documents, ask natural language questions, and receive intelligent, context-aware answers based on the document's content.

---

## 📌 Overview

The Intelligent Document Understanding Platform simplifies document analysis by enabling users to interact with PDF documents using natural language. Instead of manually searching through lengthy documents, users can simply upload a PDF and ask questions.

The application extracts text from the uploaded document, converts it into semantic embeddings using Sentence Transformers, stores them inside a FAISS vector database, retrieves the most relevant content based on the user's query, and finally uses Google Gemini to generate an accurate and contextual response.

---

# ✨ Features

- 📄 Upload PDF documents
- 📝 Extract text from PDF files
- 📊 Display document metadata
  - File Name
  - File Size
  - Number of Pages
  - Character Count
- ✂️ Split extracted text into chunks
- 🧠 Generate semantic embeddings using Sentence Transformers
- 🗂️ Store embeddings using FAISS Vector Database
- 🔍 Retrieve the most relevant document chunks
- 🤖 Generate intelligent answers using Google Gemini
- 📌 Display retrieved context for transparency
- ⚠️ Gracefully handle API and runtime errors
- ⚡ Interactive Streamlit interface

---

# 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| Streamlit | Web Application Framework |
| Google Gemini API | Large Language Model |
| Sentence Transformers | Text Embeddings |
| FAISS | Vector Database |
| PyPDF | PDF Text Extraction |
| NumPy | Numerical Operations |
| python-dotenv | Environment Variable Management |

---

# 📂 Project Structure

```text
Intelligent-Document-Understanding-Platform/
│
├── app.py
├── requirements.txt
├── README.md
├── .env.example
├── uploads/
│   └── .gitkeep
├── vectorstore/
└── utils/
    ├── pdf_loader.py
    ├── embeddings.py
    └── vector_db.py
```

---

# 📸 Application Screenshots

## 🏠 Home Page

> *(Add screenshot here)*

```markdown
![Home](assets/home.png)
```

---

## 📤 Upload PDF

> *(Add screenshot here)*

```markdown
![Upload](assets/upload.png)
```

---

## 🤖 AI Generated Answer

> *(Add screenshot here)*

```markdown
![Result](assets/result.png)
```

---

# ⚙️ Installation

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/bhavanasudhakar29/Intelligent-Document-Understanding-Platform.git
```

---

## 2️⃣ Navigate to the Project

```bash
cd Intelligent-Document-Understanding-Platform
```

---

## 3️⃣ Create a Virtual Environment (Recommended)

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 5️⃣ Configure Environment Variables

Create a `.env` file inside the project root.

```env
GOOGLE_API_KEY=YOUR_GEMINI_API_KEY
```

---

## 6️⃣ Run the Application

```bash
streamlit run app.py
```

The application will open at:

```
http://localhost:8501
```

---

# 🚀 Live Demo

Try the deployed application here:

### 🌐 https://intelligent-document-understanding-platform-eettqdhowlcigetke4.streamlit.app/

---

# 🔄 Workflow

```text
             Upload PDF
                  │
                  ▼
         Extract Text from PDF
                  │
                  ▼
        Split Text into Chunks
                  │
                  ▼
Generate Sentence Transformer Embeddings
                  │
                  ▼
 Store Embeddings using FAISS Database
                  │
                  ▼
      User asks a Question
                  │
                  ▼
Retrieve Relevant Document Chunks
                  │
                  ▼
      Google Gemini Generates Answer
                  │
                  ▼
 Display Context-Aware Response
```

---

# 🧠 How It Works

1. Upload a PDF document.
2. Extract all textual content from the document.
3. Split the extracted text into manageable chunks.
4. Convert text chunks into vector embeddings.
5. Store embeddings inside the FAISS vector database.
6. User submits a natural language question.
7. Retrieve the most relevant document chunks.
8. Send the retrieved context along with the question to Google Gemini.
9. Display the AI-generated answer along with the retrieved context.

---

# 📦 Dependencies

```
streamlit
google-generativeai
python-dotenv
sentence-transformers
pypdf
faiss-cpu
numpy
```

---

# 🚀 Future Enhancements

- 📄 Support DOCX files
- 📄 Support TXT files
- 📚 Multi-document search
- 💬 Chat history
- 👤 User authentication
- ☁️ Cloud storage integration
- 📊 Document summarization
- 🌍 Multi-language document support
- 🎤 Voice-based document querying

---

# 🤝 Contributing

Contributions are welcome!

1. Fork this repository.
2. Create a new branch.

```bash
git checkout -b feature-name
```

3. Commit your changes.

```bash
git commit -m "Added new feature"
```

4. Push your branch.

```bash
git push origin feature-name
```

5. Open a Pull Request.

---

# 📜 License

This project is licensed under the **MIT License**.

---

# 👩‍💻 Author

## **Bhavana Sudhakar**

🎓 B.Tech Artificial Intelligence & Data Science

🔗 GitHub: https://github.com/bhavanasudhakar29

---

# ⭐ If you found this project useful, don't forget to Star the repository!

⭐ **Thank you for visiting this repository!**
