from sentence_transformers import SentenceTransformer

class Embedder:

    def __init__(self):
        self.model = SentenceTransformer("paraphrase-MiniLM-L3-v2")

    def embed(self, texts):
        return self.model.encode(texts)