from services.ats_service import ATSService

resume_skills = [
    "python",
    "sql",
    "docker",
    "aws",
    "git"
]

required_skills = [
    "python",
    "sql",
    "docker",
    "aws",
    "fastapi",
    "kubernetes"
]

result = ATSService.calculate_score(
    resume_skills,
    required_skills
)

print("=" * 50)
print("ATS RESULT")
print("=" * 50)
print("Score:", result["score"])
print()
print("Matched Skills:")
print(result["matched_skills"])
print()
print("Missing Skills:")
print(result["missing_skills"])
