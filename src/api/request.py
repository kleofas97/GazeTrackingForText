from pydantic import BaseModel
from typing import Optional
class AnalyzeRequest(BaseModel):
    video_path: str
    max_x: Optional[int] = 1920

class HealthcheckRequest(BaseModel):
    video_path: str

