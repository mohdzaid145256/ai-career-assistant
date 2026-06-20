class SkillExtractorService:

    SKILLS = [
        "python",
        "java",
        "sql",
        "fastapi",
        "flask",
        "django",
        "docker",
        "kubernetes",
        "aws",
        "azure",
        "gcp",
        "terraform",
        "jenkins",
        "github actions",
        "git",
        "linux",
        "mongodb",
        "postgresql",
        "mysql",
        "redis",
        "kafka",
        "spark",
        "airflow",
        "tableau",
        "power bi",
        "pandas",
        "numpy",
        "scikit-learn",
        "tensorflow",
        "pytorch",
        "opencv",
        "machine learning",
        "deep learning",
        "nlp",
        "computer vision",
        "rag",
        "langchain",
        "llamaindex",
        "openai",
        "gemini",
        "llm",
        "prompt engineering",
        "vector database",
        "faiss",
        "pinecone",
        "weaviate",
        "mlops",
        "streamlit",
        "gradio",
        "react",
        "next.js",
        "javascript",
        "typescript",
        "html",
        "css",
        "node.js",
        "rest api",
        "graphql"
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
