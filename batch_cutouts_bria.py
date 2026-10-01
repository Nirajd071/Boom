import os
import time
import shutil
from PIL import Image
import rembg

PICTURES_DIR = "/home/niraj/dii-birthday-website/pictures"
OUTPUT_DIR = "/home/niraj/dii-birthday-website/pictures_cutouts"
SCRATCH_DIR = "/home/niraj/.gemini/antigravity/scratch/dii-birthday-website/pictures_cutouts"
BRAIN_DIR = "/home/niraj/.gemini/antigravity/brain/890f859f-ad6c-4b3f-aa2d-40ee09ecd289/cutouts"

os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(SCRATCH_DIR, exist_ok=True)
os.makedirs(BRAIN_DIR, exist_ok=True)

print("🌟 Initializing high-precision BRIA-RMBG model on CPU...")
t0 = time.time()
session = rembg.new_session("bria-rmbg")
print(f"✅ Session initialized in {time.time()-t0:.2f}s")

images = sorted([f for f in os.listdir(PICTURES_DIR) if f.lower().endswith(('.jpg', '.jpeg', '.png'))])
print(f"\nProcessing {len(images)} images for full-body & clothing preservation:\n")

total_start = time.time()
for idx, filename in enumerate(images, 1):
    input_path = os.path.join(PICTURES_DIR, filename)
    base_name = os.path.splitext(filename)[0]
    if base_name.endswith('.jpg'):
        base_name = os.path.splitext(base_name)[0]
    output_filename = f"{base_name}_cutout.png"
    output_path = os.path.join(OUTPUT_DIR, output_filename)
    scratch_path = os.path.join(SCRATCH_DIR, output_filename)
    brain_path = os.path.join(BRAIN_DIR, output_filename)

    img_start = time.time()
    img = Image.open(input_path)
    
    # Process cutout with bria-rmbg
    cutout = rembg.remove(img, session=session)
    cutout.save(output_path, "PNG")
    shutil.copy2(output_path, scratch_path)
    shutil.copy2(output_path, brain_path)

    elapsed = time.time() - img_start
    print(f"[{idx}/{len(images)}] ✨ {filename} -> {output_filename} ({elapsed:.2f}s)")

total_elapsed = time.time() - total_start
print(f"\n🎉 All {len(images)} high-definition cutouts generated successfully in {total_elapsed:.2f}s!")
