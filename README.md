# Resume / Job Description Matcher

A simple Python tool that uses Claude (Anthropic's AI) to compare your resume against a job description. It gives you:

- A match score (0-100)
- A list of important keywords/skills missing from your resume
- Specific suggestions to improve your resume for that job

## How It Works

1. You provide your resume and a job description as `.txt` files.
2. The script sends both to Claude via the Anthropic API.
3. Claude analyzes the fit and returns a detailed report.
4. The report is printed to the screen and saved as `analysis_result.txt`.

## Setup

### 1. Clone this repository
\`\`\`bash
git clone https://github.com/YOUR_USERNAME/resume-matcher.git
cd resume-matcher
\`\`\`

### 2. Install dependencies
\`\`\`bash
pip install -r requirements.txt
\`\`\`

### 3. Get an Anthropic API key
- Sign up at console.anthropic.com
- Create an API key

### 4. Set your API key as an environment variable

**Mac/Linux:**
\`\`\`bash
export ANTHROPIC_API_KEY="your-key-here"
\`\`\`

**Windows (Command Prompt):**
\`\`\`bash
setx ANTHROPIC_API_KEY "your-key-here"
\`\`\`

## Usage

\`\`\`bash
python matcher.py
\`\`\`

Sample files (`sample_resume.txt` and `sample_job.txt`) are included so you can test it right away.

## Tech Stack
- Python 3
- Anthropic API (Claude)

## Future Improvements
- Support PDF/Word resume uploads
- Web interface using Streamlit or Flask
- Batch comparison against multiple job postings