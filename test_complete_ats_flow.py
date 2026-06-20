from database.session import SessionLocal

from services.skill_service import (
    SkillService
)

from services.job_description_parser import (
    JobDescriptionParser
)

from services.ats_service import (
    ATSService
)

db = SessionLocal()

resume_skills = [
    skill.skill_name
    for skill in SkillService.get_resume_skills(
        db=db,
        resume_id=2
    )
]

job_description = """
We are looking for a Backend Engineer
with experience in Python, FastAPI,
PostgreSQL, Docker, AWS, Git and Linux.

Experience with Machine Learning
and TensorFlow is preferred.
"""

required_skills = (
    JobDescriptionParser
    .extract_required_skills(
        job_description
    )
)

result = ATSService.calculate_score(
    resume_skills,
    required_skills
)

print("=" * 50)
print("COMPLETE ATS REPORT")
print("=" * 50)

print("Score:", result["score"])

print("\nMatched Skills:")
for skill in result["matched_skills"]:
    print(skill)

print("\nMissing Skills:")
for skill in result["missing_skills"]:
    print(skill)

db.close()

