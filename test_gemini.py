from services.gemini_service import (
    GeminiService
)

response = GeminiService.generate_response(
    "Explain FastAPI in 3 lines."
)

print(response)
