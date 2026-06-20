from services.job_description_parser import (
    JobDescriptionParser
)

job_description = """
Python
FastAPI
AWS
Docker
Kubernetes
Redis
Terraform
LangChain
OpenAI
MLOps
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
