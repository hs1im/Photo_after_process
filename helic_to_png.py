import os
from PIL import Image

def convert_heic_to_png(heic_file, png_file):
    img = Image.open(heic_file)
    img.save(png_file, 'PNG')

source=""
dest=""

for filename in os.listdir(path):
    if filename.endswith('.heic') or filename.endswith('.HEIC'):
        heic_file = os.path.join(path, filename)
        png_file = os.path.join(path, os.path.splitext(filename)[0] + '.png')
        convert_heic_to_png(heic_file, png_file)