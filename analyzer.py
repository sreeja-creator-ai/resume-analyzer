import json, os
from groq import Groq

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

def analyze(resume_text: str, job_description: str) -> dict:
    prompt = f"""
You are a professional resume reviewer.

RESUME:
{resume_text[:3000]}

JOB DESCRIPTION:
{job_description[:2000]}

Return ONLY a valid JSON object with no extra text, no markdown, no backticks. Just the raw JSON:
{{
  "match_score": <number 0-100>,
  "strengths": ["point 1", "point 2", "point 3"],
  "gaps": ["missing skill 1", "missing skill 2"],
  "missing_keywords": ["keyword1", "keyword2", "keyword3"],
  "rewrite_tip": "One specific sentence to improve the resume summary."
}}
"""
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=1000
    )
    raw = response.choices[0].message.content.strip()
    
    # Clean any markdown if present
    if "```" in raw:
        raw = raw.split("```")[1]
        if raw.startswith("json"):
            raw = raw[4:]
    
    # Find JSON object in response
    start = raw.find("{")
    end = raw.rfind("}") + 1
    if start != -1 and end != 0:
        raw = raw[start:end]
    
    return json.loads(raw)
