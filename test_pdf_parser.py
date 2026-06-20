from services.pdf_parser_service import PDFParserService

text = PDFParserService.extract_text(
    "/Users/mohdzaid/Kristalball_AI_Project/Business Context and Model Summary.pdf"
)

print("=" * 50)
print("TEXT LENGTH:", len(text))
print("=" * 50)
print(text[:1000])
