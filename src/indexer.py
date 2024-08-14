from llama_index.core import VectorStoreIndex, ServiceContext
from llama_index.vector_stores.qdrant import QdrantVectorStore
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from qdrant_client import QdrantClient
from config import COLLECTION_NAME, EMBEDDING_MODEL

def create_index(documents, llm):
    client =  QdrantClient(":memory:")
    vector_store = QdrantVectorStore(client=client, collection_name=COLLECTION_NAME)
    embed_model = HuggingFaceEmbedding(model_name=EMBEDDING_MODEL)
    
    service_context = ServiceContext.from_defaults(
        llm=llm,
        embed_model=embed_model
    )
    
    index = VectorStoreIndex.from_documents(
        documents,
        service_context=service_context,
        vector_store=vector_store
    )
    
    return index