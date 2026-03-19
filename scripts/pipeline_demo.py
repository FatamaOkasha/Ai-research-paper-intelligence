import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from backend.services.paper_analysis_service import PaperAnalysisService

service = PaperAnalysisService()

result = service.analyze("data/raw_papers/sample_paper.pdf")

print(result)