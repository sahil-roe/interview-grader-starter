# Interview Grader

A tool for evaluating LLM outputs against reference answers using configurable graders.

## Quick Start

### Backend

```bash
cd backend
uv sync
uv run python seed.py        # seed 5 sample jobs
uv run uvicorn main:app --reload --port 8001
```

API runs at http://127.0.0.1:8001. Docs at http://127.0.0.1:8001/docs.

Score model graders require `OPENAI_API_KEY` in the backend environment.

### Frontend

```bash
cd frontend
npm install
npm run dev
```

App runs at http://localhost:3001.

---

## Your Task

Build a grader system on top of this app. A **grader** takes a model's output and a reference answer and returns a score between 0 and 1. Read the [OpenAI graders guide](https://developers.openai.com/api/docs/guides/graders) — your implementation should support the two types described there: `text_similarity` and `score_model`.

The starter includes both free-text outputs and JSON outputs so your graders can handle whole-answer comparisons as well as field-level comparisons.

### Requirements

1. **Reference answers** — Users can add or update the reference answer for a job.

2. **Grader configuration** — Users can create and save grader configs. A config captures the grader type and its parameters (e.g. which similarity metric to use, or which model and prompt to use as a judge). A config can be run against any job.

3. **Run a grader** — Users can run a saved grader config against a job. The app computes a score in [0, 1] and records whether it passed a configurable threshold. The result is visible on the job detail page.

4. **Text similarity grader** — Implement scoring based on string similarity between the model output and reference answer. Support at least fuzzy matching.

5. **Score model grader** — Implement an LLM-as-judge grader that sends the model output and reference answer to an OpenAI model and asks it to return a numeric score. The grader prompt should be configurable per grader config.

6. **Grader run history** — The job detail page shows all past grader runs for that job — which grader was used, the score, and whether it passed.

7. **Run all jobs** — Users can run a grader config across all jobs at once and see a summary of results.

### Constraints

- Build on the existing codebase — don't rewrite from scratch
- Use the existing patterns you see in the code

### You have 55 minutes. Prioritize what you think matters most. You should use AI tools to help you.

We're evaluating how you plan, design, interact with AI, and build — not just the final output.
