from database import Base, SessionLocal, engine
from models import Job

Base.metadata.create_all(bind=engine)

JOBS = [
    {
        "title": "Capital city — correct answer",
        "prompt": "What is the capital of Japan?",
        "model_output": "The capital of Japan is Tokyo.",
    },
    {
        "title": "Capital city — wrong answer",
        "prompt": "What is the capital of Australia?",
        "model_output": "The capital of Australia is Sydney.",
    },
    {
        "title": "Code generation — exact match",
        "prompt": "Write a Python one-liner to reverse a list called `items`.",
        "model_output": "items[::-1]",
    },
    {
        "title": "Open-ended explanation — partial credit",
        "prompt": "Explain what a neural network is in 1–2 sentences.",
        "model_output": (
            "A neural network is a computational model loosely inspired by the human brain, "
            "consisting of interconnected nodes arranged in layers that transform inputs into "
            "outputs through learned weights."
        ),
    },
    {
        "title": "Math — equivalent notation",
        "prompt": "What is the derivative of f(x) = x³ + 2x² − 5x + 1?",
        "model_output": "f'(x) = 3x^2 + 4x - 5",
    },
]


def seed():
    db = SessionLocal()
    try:
        if db.query(Job).count() > 0:
            print("Database already seeded — skipping.")
            return
        for job_data in JOBS:
            db.add(Job(**job_data))
        db.commit()
        print(f"Seeded {len(JOBS)} jobs.")
    finally:
        db.close()


if __name__ == "__main__":
    seed()
