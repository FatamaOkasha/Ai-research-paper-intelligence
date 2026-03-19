from backend.embeddings.embedder import Embedder

class SemanticSearch:

    def __init__(self, store):

        self.store = store

        self.embedder = Embedder()

    def search(self, query):

        vector = self.embedder.embed([query])[0]

        results = self.store.search(vector)

        return results