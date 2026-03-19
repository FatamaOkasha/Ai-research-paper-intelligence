class SectionExtractor:

    def extract_sections(self, text):

        sections = {
            "introduction": "",
            "method": "",
            "results": "",
            "conclusion": ""
        }

        lower = text.lower()

        if "introduction" in lower:
            sections["introduction"] = text.split("introduction")[1][:2000]

        if "conclusion" in lower:
            sections["conclusion"] = text.split("conclusion")[1][:1000]

        return sections