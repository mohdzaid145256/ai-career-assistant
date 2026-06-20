class InterviewQuestionService:

    QUESTIONS = {

        "python": [
            "What are Python decorators?",
            "What is the difference between list and tuple?",
            "Explain generators in Python.",
            "What are Python virtual environments?",
            "Explain OOP concepts in Python."
        ],

        "fastapi": [
            "What is FastAPI?",
            "How does dependency injection work in FastAPI?",
            "How do you secure FastAPI APIs?",
            "What are middleware in FastAPI?",
            "Difference between FastAPI and Flask?"
        ],

        "docker": [
            "What is Docker?",
            "Difference between image and container?",
            "What is Docker Compose?",
            "How do you optimize Docker images?",
            "Explain Docker networking."
        ],

        "aws": [
            "What is AWS?",
            "What is EC2?",
            "What is S3?",
            "Difference between EC2 and Lambda?",
            "What is IAM?"
        ],

        "machine learning": [
            "What is overfitting?",
            "What is underfitting?",
            "Difference between supervised and unsupervised learning?",
            "What is cross validation?",
            "Explain bias-variance tradeoff."
        ]
    }

    @staticmethod
    def get_questions(
        skill: str
    ):
        return (
            InterviewQuestionService
            .QUESTIONS
            .get(
                skill.lower(),
                ["No questions available for this skill"]
            )
        )
