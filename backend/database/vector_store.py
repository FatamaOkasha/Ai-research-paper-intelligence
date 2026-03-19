import faiss
import numpy as np


class VectorStore:

    def __init__(self):

        self.dimension = 384
        self.index = faiss.IndexFlatL2(self.dimension)

        self.text_chunks = []


    def add(self, embeddings, chunks):

        embeddings = np.array(embeddings).astype("float32")

        if len(embeddings) == 0:
            return

        self.index.add(embeddings)

        self.text_chunks.extend(chunks)


    def search(self, query_embedding, k=2):

        if len(self.text_chunks) == 0:
            return []

        query_embedding = np.array(query_embedding).astype("float32")

        # make sure k is not bigger than stored chunks
        k = min(k, len(self.text_chunks))

        distances, indices = self.index.search(query_embedding, k)

        results = []

        for idx in indices[0]:

            if idx >= 0 and idx < len(self.text_chunks):

                results.append(self.text_chunks[idx])

        return results