from pypdf import PdfReader


def extract_text_from_pdf(uploaded_file):
    """
    Extract text and metadata from uploaded PDF.
    """

    pdf = PdfReader(uploaded_file)

    text = ""

    for page in pdf.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    metadata = {
        "file_name": uploaded_file.name,
        "file_size": uploaded_file.size,
        "pages": len(pdf.pages),
        "characters": len(text)
    }

    return text, metadata


def split_text(text, chunk_size=500, overlap=100):
    """
    Split text into overlapping chunks.
    """

    chunks = []

    start = 0

    while start < len(text):

        end = start + chunk_size

        chunks.append(text[start:end])

        start += chunk_size - overlap

    return chunks