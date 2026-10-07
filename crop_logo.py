from PIL import Image
import os

filepath = '/Users/cuneytelgin/.gemini/antigravity/scratch/hrsolutionx/assets/images/logo.png'

if os.path.exists(filepath):
    img = Image.open(filepath)
    img = img.convert("RGBA")
    
    # Get bounding box of non-transparent pixels
    bbox = img.getbbox()
    if bbox:
        cropped_img = img.crop(bbox)
        cropped_img.save(filepath)
        print(f"Image cropped successfully. New size: {cropped_img.size}")
    else:
        print("Image is entirely transparent?")
else:
    print("File not found")

