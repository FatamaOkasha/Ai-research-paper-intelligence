from transformers import pipeline


class Summarizer:

    def __init__(self):

        self.model = pipeline(
            "summarization",
            model="sshleifer/distilbart-cnn-12-6",
            device=-1
        )

    def structured_summary(self, text):

        text = text[:4000]  # limit length to speed up

        result = self.model(
            text,
            max_length=150,
            min_length=50,
            do_sample=False
        )

        summary = result[0]["summary_text"]

        return summary