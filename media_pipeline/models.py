from pydantic import BaseModel
from typing import List

class SlideInput(BaseModel):
    text: str
    image_prompt: str

class VideoRequest(BaseModel):
    title: str
    slides: List[SlideInput]
