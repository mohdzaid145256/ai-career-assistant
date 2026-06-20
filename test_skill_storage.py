from database.session import SessionLocal

from services.skill_extractor_service import (
    SkillExtractorService
)

from services.skill_service import (
    SkillService
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

db = SessionLocal()

skills = SkillExtractorService.extract_skills(
    sample_text
)

for skill in skills:
    SkillService.create_skill(
        db=db,
        resume_id=2,
        skill_name=skill
    )

saved_skills = SkillService.get_resume_skills(
    db=db,
    resume_id=2
)

print("=" * 50)
print("SKILLS STORED")
print("=" * 50)

for skill in saved_skills:
    print(skill.skill_name)

print("=" * 50)
print("TOTAL:", len(saved_skills))

db.close()
