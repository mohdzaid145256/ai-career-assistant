class RecommendationService:

    @staticmethod
    def generate_recommendations(
        missing_skills
    ):
        recommendations = []

        for skill in missing_skills:
            recommendations.append(
                f"Add {skill} experience or projects to your resume"
            )

        return recommendations
