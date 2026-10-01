import os
import time
from PIL import Image
import rembg
import shutil

PICTURES_DIR = "/home/niraj/dii-birthday-website/pictures"
OUTPUT_DIR = "/home/niraj/dii-birthday-website/pictures_cutouts"
SCRATCH_OUTPUT_DIR = "/home/niraj/.gemini/antigravity/scratch/dii-birthday-website/pictures_cutouts"

os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(SCRATCH_OUTPUT_DIR, exist_ok=True)

print("🚀 Loading u2net model with CUDAExecutionProvider on RTX 2050...")
t0 = time.time()
session = rembg.new_session('u2net', providers=['CUDAExecutionProvider'])
print(f"✅ Session initialized in {time.time()-t0:.2f}s")
print(f"Active providers: {session.inner_session.get_providers()}")

images = sorted([f for f in os.listdir(PICTURES_DIR) if f.lower().endswith(('.jpg', '.jpeg', '.png'))])
print(f"\nFound {len(images)} images to process:\n")

total_start = time.time()
for idx, filename in enumerate(images, 1):
    input_path = os.path.join(PICTURES_DIR, filename)
    base_name = os.path.splitext(filename)[0]
    # Remove secondary extension if present (e.g. .jpg.jpeg)
    if base_name.endswith('.jpg'):
        base_name = os.path.splitext(base_name)[0]
    output_filename = f"{base_name}_cutout.png"
    output_path = os.path.join(OUTPUT_DIR, output_filename)
    scratch_path = os.path.join(SCRATCH_OUTPUT_DIR, output_filename)

    img_start = time.time()
    img = Image.open(input_path)
    
    # Process cutout on GPU
    cutout = rembg.remove(img, session=session)
    cutout.save(output_path, "PNG")
    shutil.copy2(output_path, scratch_path)

    elapsed = time.time() - img_start
    print(f"[{idx}/{len(images)}] ⚡ {filename} -> {output_filename} ({elapsed:.2f}s)")

total_elapsed = time.time() - total_start
print(f"\n🎉 All {len(images)} transparent cutouts generated successfully in {total_elapsed:.2f}s!")
