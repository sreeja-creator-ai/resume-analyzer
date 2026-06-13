# AI Resume Analyzer

An AI-powered web app that analyzes your resume against a job description and returns a match score, skill gaps, missing keywords, and rewrite suggestions.

## 🚀 Live Demo
[Click here to try it live]https://resume-analyzer-ma4i.onrender.com/)

## 🖥️ Screenshot
![App Screenshot](https://1drv.ms/i/c/ec4b5bee7d70fdba/IQAlDLHrHRMWQ7-odhP7Tmr4AZmLOXw-Ts2pIAqk5SqWhvg?e=PTW6hI)

## 🛠️ Tech Stack
- **Python 3.12**
- **FastAPI** — backend REST API
- **Groq API (LLaMA 3.3 70B)** — AI-powered analysis
- **pdfplumber** — PDF text extraction
- **python-docx** — DOCX text extraction
- **Vanilla JS + HTML/CSS** — frontend UI

## ✨ Features
- Upload resume as PDF or DOCX
- Paste any job description
- Get AI match score (0–100%)
- View strengths and skill gaps
- See missing keywords highlighted
- Get a personalized resume rewrite tip

## 📁 Project Structure
resume-analyzer/

├── main.py            # FastAPI server

├── analyzer.py        # Groq LLM analysis logic

├── resume_parser.py   # PDF/DOCX text extraction

├── requirements.txt   # Dependencies

└── frontend/

└── index.html     # UI
