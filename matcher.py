"""
Resume / Job Description Matcher
----------------------------------
Compares a resume against a job description using the Anthropic API.
Returns a match score, missing keywords, and suggestions to improve the resume.

Usage:
    python matcher.py
"""

import os
from anthropic import Anthropic


def read_file(path):
    """Read text content from a .txt file."""
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def analyze_match(resume_text, job_description_text, client):
    """Send resume + job description to Claude and get a structured analysis."""

    prompt = f"""You are a career coach helping someone tailor their resume to a job posting.

RESUME:
{resume_text}

JOB DESCRIPTION:
{job_description_text}

Please provide:
1. A match score from 0-100 (how well the resume fits the job).
2. A list of important keywords/skills from the job description that are MISSING from the resume.
3. 3-5 specific, actionable suggestions to improve the resume for this job.

Format your response clearly with headers for each section."""

    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1000,
        messages=[{"role": "user", "content": prompt}]
    )

    return response.content[0].text


def main():
    print("=== Resume / Job Description Matcher ===\n")

    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("ERROR: Please set your ANTHROPIC_API_KEY environment variable.")
        print("Example (Mac/Linux): export ANTHROPIC_API_KEY='your-key-here'")
        print("Example (Windows):   setx ANTHROPIC_API_KEY \"your-key-here\"")
        return

    client = Anthropic(api_key=api_key)

    resume_path = input("Enter path to your resume (.txt file): ").strip()
    job_path = input("Enter path to the job description (.txt file): ").strip()

    try:
        resume_text = read_file(resume_path)
        job_text = read_file(job_path)
    except FileNotFoundError as e:
        print(f"\nError: Could not find file - {e}")
        return

    print("\nAnalyzing... (this may take a few seconds)\n")

    result = analyze_match(resume_text, job_text, client)
    print(result)

    with open("analysis_result.txt", "w", encoding="utf-8") as f:
        f.write(result)
    print("\n✅ Analysis saved to analysis_result.txt")


if __name__ == "__main__":
    main()