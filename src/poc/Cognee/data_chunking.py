import cognee
import asyncio
from pydantic import BaseModel
from cognee import Task, Pipeline


# Define Datapoints
class DocumentData(BaseModel):
    content: str


class ChunkData(BaseModel):
    chunks: list[str]


# Define a simple chunking task
class ChunkingTask(Task):
    def run(self, doc: DocumentData) -> ChunkData:
        # Example: split by double newlines
        chunks = doc.content.split("\n\n")
        return ChunkData(chunks=chunks)


async def main():
    # Reset Cognee state
    await cognee.prune.prune_data()
    await cognee.prune.prune_system(metadata=True)

    text = """
    Natural language processing (NLP) is an interdisciplinary
    subfield of computer science and information retrieval.

    NLP techniques are used to analyze text, allowing machines to
    understand human language.
    """

    # Add text to Cognee
    await cognee.add(text)

    # Create a pipeline with just the chunking task for demonstration
    chunking_pipeline = Pipeline([ChunkingTask()])

    # Retrieve the added document from Cognee as DocumentData
    # (In practice, this might be part of a pipeline or a retrieval task.)
    doc_data = DocumentData(content=text.strip())

    # Run the pipeline to chunk the document
    chunk_data = chunking_pipeline.run(doc_data)
    print("Chunks:", chunk_data.chunks)


if __name__ == '__main__':
    asyncio.run(main())