from services.job_description_parser import (
    JobDescriptionParser
)

job_description = """
We are looking for a Backend Engineer
with experience in Python, FastAPI,
PostgreSQL, Docker, AWS, Git and Linux.

Experience with Machine Learning
and TensorFlow is preferred.
"""

skills = (
    JobDescriptionParser
    .extract_required_skills(
        job_description
    )
)

print("=" * 50)
print("JOB DESCRIPTION SKILLS")
print("=" * 50)

for skill in skills:
    print(skill)

print("=" * 50)
print("TOTAL:", len(skills))
