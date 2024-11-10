import os

# Paths
current_dir = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(current_dir, "data")
PDF_DIR = os.path.join(DATA_DIR, "pdfs")
TEXT_DIR = os.path.join(DATA_DIR, "texts")
CHROMA_PATH = os.path.join(DATA_DIR, "chroma")

# Models
EMBEDDING_MODEL = "nomic-embed-text"
LLM_MODEL = "mistral"

# Prompt options
PROMPT_TEMPLATE = """
Answer the question based only on the following context:

{context}

---

Answer the question based on the above context: {question}
"""

# Database options
K = 5
CHUNK_SIZE = 800
CHUNK_OVERLAP = 80
