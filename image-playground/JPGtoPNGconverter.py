import sys
import os
from PIL import Image 
'''
JPG to PNG Pokedex Converter
usage: python3 JPGtoPNGconverter.py Pokedex/ new/
'''

# use sys module: grab first and second argument
image_folder = sys.argv[1]
output_folder = sys.argv[2]

print(image_folder, output_folder)

# use os module: check if new/ exists, if not create
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
    
# loop through Pokedex
# convert images to png
# save to the new folders
for filename in os.listdir(image_folder):
    img = Image.open(f'{image_folder}{filename}')
    clean_name = os.path.splitext(filename)[0]
    img.save(f'{output_folder}{clean_name}.png','png')
    print('all done')
    # print(clean_name)