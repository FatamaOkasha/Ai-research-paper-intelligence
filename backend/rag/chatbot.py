from transformers import pipeline
from backend.embeddings.embedder import Embedder


class PaperChatbot:

    def __init__(self, vector_store):

        self.vector_store = vector_store
        self.embedder = Embedder()

        # small fast QA model
        self.qa_model = pipeline(
            "text2text-generation",
            model="google/flan-t5-small",
            device=-1
        )

    def answer(self, question):

        # make sure papers exist
        if len(self.vector_store.text_chunks) == 0:
            return "Please analyze papers first."

        # embed question
        query_embedding = self.embedder.embed([question])

        # retrieve chunks
        chunks = self.vector_store.search(query_embedding, k=2)

        if len(chunks) == 0:
            return "No relevant information found in the papers."

        # limit context size to avoid token overflow
        context = "\n\n".join(chunks)[:1500]

        prompt = f"""
You are an AI research assistant.

Use ONLY the information from the research papers below.
If the answer is not found in the papers, say:
"The papers do not mention this."

Context:
{context}

Question:
{question}

Answer:
"""

        result = self.qa_model(prompt, max_length=120)

        answer = result[0]["generated_text"].replace("Answer:", "").strip()

        source = chunks[0][:250]

        return f"""
Answer:
{answer}

Source from paper:
{source}
"""