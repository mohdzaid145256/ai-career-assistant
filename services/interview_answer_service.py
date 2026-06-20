class InterviewAnswerService:

    ANSWERS = {

        "What is FastAPI?":
        """
        FastAPI is a modern Python web framework
        used for building high-performance APIs.

        It is based on Python type hints and
        automatically generates API documentation
        using Swagger UI and ReDoc.

        FastAPI provides validation,
        serialization and excellent performance.
        """,

        "What is Docker?":
        """
        Docker is a containerization platform
        used to package applications and their
        dependencies into portable containers.

        This ensures consistent deployment
        across development, testing and
        production environments.
        """,

        "What is AWS?":
        """
        AWS is Amazon Web Services,
        a cloud computing platform that
        provides services such as EC2,
        S3, Lambda, RDS and many others.

        It helps organizations deploy and
        scale applications efficiently.
        """
    }

    @staticmethod
    def get_answer(
        question: str
    ):
        return (
            InterviewAnswerService
            .ANSWERS
            .get(
                question,
                "Answer not available."
            )
        )
