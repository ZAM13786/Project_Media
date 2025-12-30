from fastapi import FastAPI, HTTPException
from models import VideoRequest
from audio_generator import generate_audio_for_slides
from image_generator import generate_slide_images
from video_compiler import compile_video

app = FastAPI()

@app.post("/generate-video")
def generate_video(req: VideoRequest):
    try:
        slide_texts = [s.text for s in req.slides]
        base_name = req.title.replace(" ", "_")

        audio_paths = generate_audio_for_slides(slide_texts, base_name)
        image_paths = generate_slide_images(req.title, slide_texts, base_name)
        video_path = compile_video(image_paths, audio_paths, base_name + "_final")

        return {
            "status": "success",
            "video_path": video_path
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
