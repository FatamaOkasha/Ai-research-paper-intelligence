from backend.retrieval.semantic_search import SemanticSearch

class RAGPipeline:

    def __init__(self, store):

        self.search = SemanticSearch(store)

    def answer(self, question):

        contexts = self.search.search(question)

        response = "Relevant paper segments:\n\n"

        for c in contexts:

            response += c[:300] + "\n\n"

        return response