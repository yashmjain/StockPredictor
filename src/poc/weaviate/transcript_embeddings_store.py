from langchain_community.document_loaders import PythonLoader, DirectoryLoader, TextLoader

import weaviate
import weaviate.classes.config as wc

from langchain_text_splitters import CharacterTextSplitter
from langchain_weaviate.vectorstores import WeaviateVectorStore
from langchain_ollama import OllamaEmbeddings



path = "/home/yash/code/StockPredictor/data/transcribed_text/"

loader = DirectoryLoader(path, glob="hard_to_transcribe.txt", loader_cls=TextLoader)

documents = loader.load()
text_splitter = CharacterTextSplitter(chunk_size=5, chunk_overlap=0)
docs = text_splitter.split_documents(documents)



# Print the first 100 characters of each result
for i, doc in enumerate(docs):
    print(f"\nDocument {i + 1}:")
    print(doc.page_content[:100] + "...")

#doc_sources = [doc.metadata["source"] for doc in docs]

embeddings = OllamaEmbeddings( model="llama3:8b")
weaviate_client = weaviate.connect_to_local()
db = WeaviateVectorStore.from_documents(docs, embeddings, client=weaviate_client)

query = "who picked the seashells by the seashore?"
docs = db.similarity_search(query)

# Print the first 100 characters of each result
for i, doc in enumerate(docs):
    print(f"\nDocument {i + 1}:")
    print(doc.page_content[:100] + "...")
# if not weaviate_client.schema.exists("Transcript"):
#     transcript_schema = {
#         "class": "Transcript",
#         "properties": [
#             {"name": "name", "dataType": ["text"]},
#             {"name": "id", "dataType": ["text"]},
#             {"name": "youtube_link", "dataType": ["text"]},
#             {"name": "text", "dataType": ["text"]},
#         ],
#     }
#     weaviate_client.schema.create_class(transcript_schema)






