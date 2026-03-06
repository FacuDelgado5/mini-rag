from langchain_community.document_loaders import PyPDFLoader

# Load a PDF file and return its pages as documents.
def load_pdf(file_path):

    loader = PyPDFLoader(file_path)
    documents = loader.load()

    return documents