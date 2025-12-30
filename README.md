# Project_Media
# Media Automation Pipeline (Python + FastAPI)

This project is a mini media automation pipeline that generates **audio**, **slide images**, and a **final video** from structured JSON input using Python. [file:1]  
It exposes a REST API using FastAPI to trigger the pipeline and returns the path to the generated MP4 video. [file:1][web:22]

---

## Features

- Accepts structured JSON with a title and a list of slides (text + image prompt). [file:1]  
- Generates audio narration for each slide using a text‑to‑speech library (e.g. gTTS). [file:1][web:2]  
- Creates simple slide images containing the title and slide text using Pillow. [file:1][web:2]  
- Combines each slide image with its corresponding audio using MoviePy and concatenates them into a final MP4 video. [file:1][web:2]  
- Provides a `POST /generate-video` API endpoint to trigger the whole pipeline. [file:1][web:22]

---

## Project structure

media_pipeline/
├── main.py
├── models.py
├── audio_generator.py
├── image_generator.py
├── video_compiler.py
├── requirements.txt
└── output/
├── audio/
├── images/
└── video/

text

- `audio_generator.py`: functions to generate audio files from slide text. [file:1]  
- `image_generator.py`: functions to generate slide images with title and text. [file:1]  
- `video_compiler.py`: combines images and audio into a final MP4 video. [file:1]  
- `main.py`: FastAPI app exposing the `/generate-video` endpoint. [file:1][web:22]

---

## Installation

1. Create and activate a virtual environment (recommended).

python -m venv venv
source venv/bin/activate # Linux / macOS
venv\Scripts\activate # Windows

text

2. Install dependencies:

pip install -r requirements.txt

text

Typical `requirements.txt`:

fastapi
uvicorn
gTTS
Pillow
moviepy==1.0.3
pydantic

text

MoviePy uses `ffmpeg` under the hood; it will be downloaded automatically via `imageio` the first time it runs (internet required). [web:2][web:38]

---

## Running the API

Start the FastAPI server with uvicorn:

uvicorn main:app --reload

text

The API will be available at:

- Base URL: `http://127.0.0.1:8000`  
- Interactive docs (Swagger UI): `http://127.0.0.1:8000/docs` [web:22][web:40]

---

## API: `POST /generate-video`

### Request

Content-Type: `application/json`

Example body (topic: **Newton's Laws of Motion**):

{
"title": "Introduction to Newton's Laws of Motion",
"slides": [
{
"text": "Newton's first law states that an object remains at rest or in uniform motion unless acted on by an external force.",
"image_prompt": "diagram of a block on a frictionless surface with forces"
},
{
"text": "Newton's second law relates force, mass, and acceleration using the formula F equals m times a.",
"image_prompt": "free body diagram of a box being pushed with labeled forces"
},
{
"text": "Newton's third law states that for every action there is an equal and opposite reaction.",
"image_prompt": "two skaters pushing off each other on ice"
}
]
}

text

This matches the required JSON schema: a `title` string and an array of `slides` objects with `text` and `image_prompt`. [file:1]

### Response

On success:

{
"status": "success",
"video_path": "output/video/Introduction_to_Newton_s_Laws_of_Motion_final.mp4"
}

text

- `video_path` is the relative path to the generated MP4 file in the `output/video` directory. [file:1]

---

## How it works (internals)

1. The API parses the incoming JSON into Pydantic models (`VideoRequest`, `SlideInput`). [file:1][web:22]  
2. `audio_generator.generate_audio_for_slides` creates one audio file per slide text and stores them in `output/audio`. [file:1]  
3. `image_generator.generate_slide_images` creates one PNG per slide with the title and slide text and stores them in `output/images`. [file:1]  
4. `video_compiler.compile_video` uses MoviePy to pair each image with its audio and concatenate all clips into a single MP4 in `output/video`. [file:1][web:2]
