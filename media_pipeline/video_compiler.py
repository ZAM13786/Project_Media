import os
from typing import List
from moviepy.editor import ImageClip, AudioFileClip, concatenate_videoclips

VIDEO_DIR = "output/video"

os.makedirs(VIDEO_DIR, exist_ok=True)

def compile_video(image_paths: List[str], audio_paths: List[str], output_name: str) -> str:
    if len(image_paths) != len(audio_paths):
        raise ValueError("Number of images and audio files must match")

    clips = []
    try:
        for img_path, audio_path in zip(image_paths, audio_paths):
            audio_clip = AudioFileClip(audio_path)
            duration = audio_clip.duration

            img_clip = ImageClip(img_path).set_duration(duration)
            img_clip = img_clip.set_audio(audio_clip)

            clips.append(img_clip)

        final_clip = concatenate_videoclips(clips, method="compose")
        output_path = os.path.join(VIDEO_DIR, f"{output_name}.mp4")
        final_clip.write_videofile(output_path, fps=24)
        final_clip.close()
        for c in clips:
            c.close()

        return output_path
    except Exception as e:
        raise RuntimeError(f"Failed to compile video: {e}")
