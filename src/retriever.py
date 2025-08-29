from sentence_transformers import SentenceTransformer
import faiss

class Retriever:
    def __init__(self, model_name="all-MiniLM-L6-v2"):
        self.embedder = SentenceTransformer(model_name)
        self.index = None
        self.docs = []

    def add_documents(self, docs):
        self.docs.extend(docs)
        embeddings = self.embedder.encode(docs)
        dimension = embeddings.shape[1]
        if self.index is None:
            self.index = faiss.IndexFlatL2(dimension)
        self.index.add(embeddings)

    def retrieve(self, query, top_k=2):
        query_vec = self.embedder.encode([query])
        distances, indices = self.index.search(query_vec, top_k)
        return [self.docs[i] for i in indices[0]]
