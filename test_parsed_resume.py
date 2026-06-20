from database.session import SessionLocal

from services.pdf_parser_service import (
    PDFParserService
)

from services.parsed_resume_service import (
    ParsedResumeService
)

db = SessionLocal()

text = PDFParserService.extract_text(
    "/Users/mohdzaid/Kristalball_AI_Project/Business Context and Model Summary.pdf"
)

parsed_resume = ParsedResumeService.create_parsed_resume(
    db=db,
    resume_id=2,
    raw_text=text
)

print("=" * 50)
print("PARSED RESUME ID:", parsed_resume.id)
print("TEXT LENGTH:", len(parsed_resume.raw_text))
print("=" * 50)

saved_resume = ParsedResumeService.get_by_resume_id(
    db=db,
    resume_id=2
)

print("DATABASE FETCH SUCCESS")
print(saved_resume.id)
print(saved_resume.raw_text[:500])

db.close()

