import fitz  # PyMuPDF


class PDFParser:

    def parse(self, pdf_path):

        if pdf_path is None:
            raise ValueError("PDF path is None")

        text = ""

        doc = fitz.open(pdf_path)

        for page in doc:
            page_text = page.get_text()

            if page_text:
                text += page_text

        doc.close()

        return text