from backend.parser.pdf_parser import PDFParser
from backend.preprocessing.cleaner import TextCleaner
from backend.preprocessing.chunker import TextChunker

from backend.embeddings.embedder import Embedder
from backend.database.vector_store import VectorStore

from backend.summarization.summarizer import Summarizer
from backend.rag.chatbot import PaperChatbot


class PaperAnalysisService:

    def __init__(self):

        self.parser = PDFParser()
        self.cleaner = TextCleaner()
        self.chunker = TextChunker()

        self.vector_store = VectorStore()

        # lazy-loaded components
        self._embedder = None
        self._summarizer = None
        self._chatbot = None


    def get_embedder(self):

        if self._embedder is None:
            self._embedder = Embedder()

        return self._embedder


    def get_summarizer(self):

        if self._summarizer is None:
            self._summarizer = Summarizer()

        return self._summarizer


    def get_chatbot(self):

        if self._chatbot is None:
            self._chatbot = PaperChatbot(self.vector_store)

        return self._chatbot


    def analyze(self, pdf_path):

        # 1️⃣ parse PDF
        text = self.parser.parse(pdf_path)

        # 2️⃣ clean text
        clean_text = self.cleaner.clean(text)

        # 3️⃣ split text into chunks
        chunks = self.chunker.chunk(clean_text)

        # 4️⃣ generate embeddings
        embedder = self.get_embedder()
        embeddings = embedder.embed(chunks)

        # 5️⃣ store embeddings in FAISS
        self.vector_store.add(embeddings, chunks)

        # 6️⃣ summarize paper
        summarizer = self.get_summarizer()
        summary = summarizer.structured_summary(clean_text)

        return {
            "summary": summary,
            "num_chunks": len(chunks)
        }


    def answer_question(self, question):

        chatbot = self.get_chatbot()

        answer = chatbot.answer(question)

        return answer