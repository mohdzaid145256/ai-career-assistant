from services.pdf_parser_service import (
    PDFParserService
)

from services.skill_extractor_service import (
    SkillExtractorService
)

text = PDFParserService.extract_text(
    "/Users/mohdzaid/Kristalball_AI_Project/Business Context and Model Summary.pdf"
)

skills = SkillExtractorService.extract_skills(
    text
)

print("=" * 50)
print("SKILLS FOUND")
print("=" * 50)

for skill in skills:
    print(skill)

print("=" * 50)
print("TOTAL:", len(skills))
