import os
from typing import List
from PIL import Image, ImageDraw, ImageFont

IMAGE_DIR = "output/images"

os.makedirs(IMAGE_DIR, exist_ok=True)

def generate_slide_images(title: str, slide_texts: List[str], base_name: str) -> List[str]:
    image_paths = []
    width, height = 1280, 720

    try:
        font_title = ImageFont.truetype("arial.ttf", 48)
        font_text = ImageFont.truetype("arial.ttf", 32)
    except Exception:
        font_title = ImageFont.load_default()
        font_text = ImageFont.load_default()

    for idx, text in enumerate(slide_texts, start=1):
        img = Image.new("RGB", (width, height), color="white")
        draw = ImageDraw.Draw(img)

        draw.text((60, 40), title, fill="black", font=font_title)
        draw.text((60, 140), text, fill="black", font=font_text)

        filename = f"{base_name}_slide_{idx}.png"
        filepath = os.path.join(IMAGE_DIR, filename)
        img.save(filepath)
        image_paths.append(filepath)

    return image_paths
