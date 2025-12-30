import os
from gtts import gTTS
from typing import List

AUDIO_DIR = "output/audio"

os.makedirs(AUDIO_DIR, exist_ok=True)

def generate_audio_for_slides(slides: List[str], base_name: str) -> List[str]:
    audio_paths = []
    for idx, text in enumerate(slides, start=1):
        filename = f"{base_name}_slide_{idx}.mp3"
        filepath = os.path.join(AUDIO_DIR, filename)
        try:
            tts = gTTS(text=text, lang="en")
            tts.save(filepath)
            audio_paths.append(filepath)
        except Exception as e:
            raise RuntimeError(f"Failed to generate audio for slide {idx}: {e}")
    return audio_paths
