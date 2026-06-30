from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OllamaEmbeddings

print("=" * 60)
print("Loading Company Documents...")
print("=" * 60)

loader = PyPDFDirectoryLoader("data")
documents = loader.load()

print(f"Documents Loaded : {len(documents)}")

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100
)

chunks = splitter.split_documents(documents)

print(f"Total Chunks Created : {len(chunks)}")

# -----------------------------
# Add Metadata
# -----------------------------

for chunk in chunks:

    if "source" in chunk.metadata:

        file_name = chunk.metadata["source"].split("\\")[-1]

        chunk.metadata["document"] = file_name

embeddings = OllamaEmbeddings(
    model="nomic-embed-text"
)

print("Generating Embeddings...")

db = Chroma.from_documents(

    documents=chunks,

    embedding=embeddings,

    persist_directory="chroma_db"

)

print("=" * 60)
print("Documents Indexed Successfully")
print("=" * 60)

print("Indexed Documents")

unique = set()

for chunk in chunks:

    unique.add(chunk.metadata["document"])

for doc in unique:

    print("✔", doc)

print("=" * 60)