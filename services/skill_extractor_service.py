class SkillExtractorService:

    SKILLS = [
        "python",
        "java",
        "sql",
        "fastapi",
        "flask",
        "docker",
        "aws",
        "tensorflow",
        "pytorch",
        "pandas",
        "numpy",
        "git",
        "linux",
        "react",
        "mongodb",
        "postgresql",
        "mysql",
        "spark",
        "airflow",
        "tableau",
        "opencv",
        "machine learning",
        "deep learning"
    ]

    @staticmethod
    def extract_skills(
        text: str
    ):
        text_lower = text.lower()

        found_skills = []

        for skill in SkillExtractorService.SKILLS:
            if skill in text_lower:
                found_skills.append(skill)

        return list(set(found_skills))
