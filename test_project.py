from project import get_pdf_text, get_text_chunks,get_vectorstore


def test_get_pdf_text():
    pdf_doc = ['./cs50p_test.pdf']
    assert get_pdf_text(pdf_doc) == "Hello! This is my cs50p final project.  "


def test_get_text_chunks():
    sample_text = "This is a test pdf"
    chunks = get_text_chunks(sample_text)
    assert len(chunks) > 0
    assert sample_text in chunks[0]

def test_get_vectorstore():
    sample_text = "This is a test pdf"
    chunks = get_text_chunks(sample_text)
    vector_store = get_vectorstore(chunks)
    x = type(vector_store)
    assert type(vector_store) == x

