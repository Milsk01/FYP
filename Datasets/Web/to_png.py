from PIL import Image
import os
import zipfile
import shutil

for image in os.listdir('images'):
    im = Image.open(os.path.join('images',image))
    im.save(os.path.join('images',image.split('.')[0] + '.png'))
    os.remove(os.path.join('images',image))




    
