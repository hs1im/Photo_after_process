import os
import pyheif
from PIL import Image

def convert_heic_to_png(heic_file, png_file):
    heif_file = pyheif.read(heic_file)
    img = Image.frombytes(
        heif_file.mode, 
        heif_file.size, 
        heif_file.data,
        "raw",
        heif_file.mode,
        heif_file.stride,
    )
    img.save(png_file, 'PNG')

source="./Data/second_origin"
dest="./Data/second_png"

for filename in os.listdir(source):
    if filename.endswith('.heic') or filename.endswith('.HEIC'):
        heic_file = f"{source}/{filename}"
        png_file = f"{dest}/{os.path.splitext(filename)[0]}.png"
        #png_file = os.path.join(dest, os.path.splitext(filename)[0] + '.png')
        convert_heic_to_png(heic_file, png_file)