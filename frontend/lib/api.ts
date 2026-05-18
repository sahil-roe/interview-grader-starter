const API_BASE = process.env.NEXT_PUBLIC_API_URL ?? "http://127.0.0.1:8001";

export interface Job {
  id: number;
  title: string;
  prompt: string;
  model_output: string;
  created_at: string;
}

export async function listJobs(): Promise<Job[]> {
  const res = await fetch(`${API_BASE}/jobs`, { cache: "no-store" });
  if (!res.ok) throw new Error(`Failed to fetch jobs: ${res.status}`);
  return res.json();
}

export async function getJob(id: number): Promise<Job> {
  const res = await fetch(`${API_BASE}/jobs/${id}`, { cache: "no-store" });
  if (!res.ok) throw new Error(`Failed to fetch job: ${res.status}`);
  return res.json();
}
