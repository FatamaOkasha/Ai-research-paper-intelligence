class NoveltyDetector:

    def check(self, paper_text):

        if "new method" in paper_text.lower():
            return {"novelty": "Potentially novel"}

        return {"novelty": "Uncertain"}