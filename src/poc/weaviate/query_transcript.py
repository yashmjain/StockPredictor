import weaviate

weaviate_client = weaviate.connect_to_local()
weaviate_client.query

query = "What did the president say about Ketanji Brown Jackson"
docs = db.similarity_search(query)

# Print the first 100 characters of each result
for i, doc in enumerate(docs):
    print(f"\nDocument {i + 1}:")
    print(doc.page_content[:100] + "...")