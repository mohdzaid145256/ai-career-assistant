from google import genai

from core.config import settings


class GeminiService:

    @staticmethod
    def generate_response(
        prompt: str
    ):
        client = genai.Client(
            api_key=settings.GEMINI_API_KEY
        )

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text
