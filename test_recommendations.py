from services.recommendation_service import (
    RecommendationService
)

missing_skills = [
    "fastapi",
    "kubernetes",
    "docker"
]

recommendations = (
    RecommendationService
    .generate_recommendations(
        missing_skills
    )
)

print("=" * 50)
print("RECOMMENDATIONS")
print("=" * 50)

for recommendation in recommendations:
    print(recommendation)
