from backend.parser.pdf_parser import PDFParser
from backend.preprocessing.chunker import TextChunker
from backend.embeddings.embedder import Embedder


def main():

    pdf_path = "data/sample_paper.pdf"

    parser = PDFParser()
    chunker = TextChunker()
    embedder = Embedder()

    print("Reading PDF...")

    text = parser.extract_text(pdf_path)

    print("Text length:", len(text))

    print("Chunking text...")

    chunks = chunker.chunk_text(text)

    print("Number of chunks:", len(chunks))

    print("Generating embeddings...")

    vectors = embedder.embed(chunks)

    print("Embedding shape:", len(vectors))

    print("Pipeline working successfully!")


if __name__ == "__main__":
    main()