import chromadb

client = chromadb.PersistentClient(path="chroma_db")

text_collection = client.get_or_create_collection("text")
image_collection = client.get_or_create_collection("image")
