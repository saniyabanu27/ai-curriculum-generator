from fastapi import FastAPI
from pydantic import BaseModel
from curriculum_engine import generate_curriculum

app = FastAPI(title="Offline Curriculum Generator")

class CurriculumRequest(BaseModel):
    course_name: str
    level: str
    duration_weeks: int

@app.post("/generate-curriculum")
def create_curriculum(request: CurriculumRequest):
    result = generate_curriculum(
        request.course_name,
        request.level,
        request.duration_weeks
    )
    return result
