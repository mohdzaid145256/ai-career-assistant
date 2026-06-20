from services.skill_extractor_service import (
    SkillExtractorService
)

sample_text = """
Python
FastAPI
Docker
AWS
PostgreSQL
Git
Linux
Machine Learning
TensorFlow
"""

skills = SkillExtractorService.extract_skills(
    sample_text
)

print(skills)
