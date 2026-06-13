from fastapi import FastAPI, UploadFile, File, Form
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import shutil, os
from resume_parser import extract_text
from analyzer import analyze

app = FastAPI()
app.mount("/static", StaticFiles(directory="frontend"), name="static")

@app.get("/")
def root():
    return FileResponse("frontend/index.html")

@app.post("/analyze")
async def analyze_resume(
    file: UploadFile = File(...),
    job_description: str = Form(...)
):
    tmp_path = f"tmp_{file.filename}"
    with open(tmp_path, "wb") as f:
        shutil.copyfileobj(file.file, f)
    
    resume_text = extract_text(tmp_path, file.filename)
    os.remove(tmp_path)
    
    if not resume_text.strip():
        return {"error": "Could not read text from the uploaded file."}
    
    result = analyze(resume_text, job_description)
    return result