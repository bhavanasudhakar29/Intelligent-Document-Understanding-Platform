import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

from utils.pdf_loader import extract_text_from_pdf, split_text
from utils.embeddings import create_embeddings, embedding_model
from utils.vector_db import VectorStore

# ----------------------------
# Load Gemini API
# ----------------------------
load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("models/gemini-3.5-flash")

# ----------------------------
# Streamlit UI
# ----------------------------
st.set_page_config(
    page_title="DocumentAI",
    page_icon="📄",
    layout="wide"
)

st.title("📄 Intelligent Document Understanding Platform")

st.write("Upload a PDF and ask questions using AI.")

uploaded_file = st.file_uploader(
    "Upload PDF",
    type=["pdf"]
)

if uploaded_file:

    # ----------------------------
    # Extract Text + Metadata
    # ----------------------------
    text, metadata = extract_text_from_pdf(uploaded_file)

    st.success("✅ PDF Uploaded Successfully!")

    st.subheader("📄 PDF Information")

    col1, col2 = st.columns(2)

    with col1:
        st.write(f"**File Name:** {metadata['file_name']}")
        st.write(f"**Pages:** {metadata['pages']}")
        st.write(f"**Characters:** {metadata['characters']}")

    with col2:
        st.write(f"**File Size:** {round(metadata['file_size']/1024,2)} KB")

    # ----------------------------
    # Extracted Text
    # ----------------------------
    st.subheader("📄 Extracted Text")

    st.text_area(
        "Document",
        text,
        height=250
    )

    # ----------------------------
    # Chunk Text
    # ----------------------------
    chunks = split_text(text)

    st.subheader("🧩 Processing Information")

    st.write(f"**Total Chunks:** {len(chunks)}")
    st.write("**Embedding Model:** all-MiniLM-L6-v2")
    st.write("**Vector Database:** FAISS")
    st.write("**LLM:** Gemini 3.5 Flash")

    # ----------------------------
    # Create Embeddings
    # ----------------------------
    embeddings = create_embeddings(chunks)

    # ----------------------------
    # Create Vector Store
    # ----------------------------
    vector_store = VectorStore()

    vector_store.create_index(
        embeddings,
        chunks
    )

    st.divider()

    # ----------------------------
    # Ask Question
    # ----------------------------
    st.subheader("❓ Ask Question")

    question = st.text_input(
        "Enter your question"
    )

    if st.button("Get Answer"):

        if question.strip() == "":

            st.warning("Please enter a question.")

        else:

            query_embedding = embedding_model.encode(question)

            relevant_chunks = vector_store.search(
                query_embedding,
                k=3
            )

            context = "\n\n".join(relevant_chunks)

            prompt = f"""
You are an AI assistant.

Answer ONLY using the context below.

If the answer is not found, reply:

'I couldn't find the answer in the uploaded document.'

Context:

{context}

Question:

{question}
"""

            with st.spinner("🤖 Thinking..."):

                try:

                    response = model.generate_content(prompt)

                    st.success("✅ Answer")

                    st.write(response.text)

                except Exception:

                    st.error("⚠️ Gemini API quota exceeded.")
                    st.info("Please wait about one minute and try again.")

            with st.expander("📄 Retrieved Context"):

                st.write(context)