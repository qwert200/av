import os
import re
import random

import aiofiles
import aiohttp
from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont
from unidecode import unidecode
from youtubesearchpython.__future__ import VideosSearch
from AnonXMusic import app
from config import YOUTUBE_IMG_URL


def changeImageSize(maxWidth, maxHeight, image):
    widthRatio = maxWidth / image.size[0]
    heightRatio = maxHeight / image.size[1]
    newWidth = int(widthRatio * image.size[0])
    newHeight = int(heightRatio * image.size[1])
    newImage = image.resize((newWidth, newHeight))
    return newImage


def clear(text):
    list = text.split(" ")
    title = ""
    for i in list:
        if len(title) + len(i) < 60:
            title += " " + i
    return title.strip()


async def get_thumb(videoid):
    # ... (existing code)

    background = Image.new("RGB", (1280, 720), gradient_colors())
    draw = ImageDraw.Draw(background)

    arial = ImageFont.load_default()
    font = ImageFont.truetype("AnonXMusic/assets/font.ttf", 42)

    draw.text((50, 20), unidecode(app.name), fill="white", font=font)
    draw.text((30, 550), f"{channel} | {views[:23]}", "white", font=font)
    draw.text((30, 610), clear(title), "white", font=font)

    draw.line([(55, 660), (1220, 660)], fill="white", width=5, joint="curve")
    draw.ellipse([(918, 648), (942, 672)], outline="white", fill="white", width=15)

    draw.text((36, 670), "00:00", "white", font=arial)
    draw.text((1150, 670), f"{duration[:23]}", "white", font=arial)

    try:
        os.remove(f"cache/thumb{videoid}.png")
    except:
        pass

    background.save(f"cache/{videoid}.png")
    return f"cache/{videoid}.png"

def gradient_colors():
    # Add your custom gradient color generation logic here
    # Example: return [(r1, g1, b1), (r2, g2, b2)]
    return [(30, 87, 153), (0, 0, 0)]
