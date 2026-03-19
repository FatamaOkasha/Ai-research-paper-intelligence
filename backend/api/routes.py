from fastapi import APIRouter
from backend.services.paper_analysis_service import PaperAnalysisService

router = APIRouter()

service = PaperAnalysisService()

@router.post("/analyze")
def analyze(pdf_path: str):
    return service.analyze(pdf_path)