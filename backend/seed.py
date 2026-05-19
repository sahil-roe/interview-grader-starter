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
        "title": "Contact extraction — JSON output",
        "prompt": (
            "Extract the contact's name, email, and company from this text: "
            "Jane Doe from Acme Corp can be reached at jane.doe@acme.com."
        ),
        "model_output": (
            '{\n'
            '  "name": "Jane Doe",\n'
            '  "email": "jane.doe@acme.com",\n'
            '  "company": "Acme Corp"\n'
            "}"
        ),
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
        "title": "Invoice extraction — JSON output",
        "prompt": (
            "Extract invoice fields from this text: Invoice INV-1024 for $349.50 "
            "is due on 2026-06-15 and should be paid by Globex LLC."
        ),
        "model_output": (
            '{\n'
            '  "invoice_id": "INV-1024",\n'
            '  "amount": "349.50",\n'
            '  "due_date": "2026-06-15",\n'
            '  "customer": "Globex LLC"\n'
            "}"
        ),
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
