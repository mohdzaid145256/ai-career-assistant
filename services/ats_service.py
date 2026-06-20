class ATSService:

    @staticmethod
    def calculate_score(
        resume_skills,
        required_skills
    ):
        resume_set = {
            skill.lower()
            for skill in resume_skills
        }

        required_set = {
            skill.lower()
            for skill in required_skills
        }

        matched_skills = (
            resume_set &
            required_set
        )

        score = (
            len(matched_skills)
            / len(required_set)
        ) * 100

        return {
            "score": round(score, 2),
            "matched_skills": list(
                matched_skills
            ),
            "missing_skills": list(
                required_set -
                matched_skills
            )
        }
