import weaviate
import weaviate.classes.query as wq
import os


# Instantiate your client (not shown). e.g.:
# headers = {"X-OpenAI-Api-Key": os.getenv("OPENAI_APIKEY")}  # Replace with your OpenAI API key
# client = weaviate.connect_to_weaviate_cloud(..., headers=headers) or
# client = weaviate.connect_to_local(..., headers=headers)

# Get the collection
client = weaviate.connect_to_local()
movies = client.collections.get("Movie")

# Perform query
response = movies.query.near_text(
    query="dystopian future", limit=5, return_metadata=wq.MetadataQuery(distance=True)
)

# Inspect the response
for o in response.objects:
    print(
        o.properties["title"], o.properties["release_date"].year
    )  # Print the title and release year (note the release date is a datetime object)
    print(
        f"Distance to query: {o.metadata.distance:.3f}\n"
    )  # Print the distance of the object from the query

client.close()