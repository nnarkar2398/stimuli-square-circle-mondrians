#Narkar and Fenske (2023): A search for an affective index of inhibition in the narrowing of attention 
#reveals interactive effects of congruence and exposure on stimulus liking

#Code for cropping the square and circle mondrian like patterns for stimuli generation for Experiments 1-4.

#packages: 
from PIL import Image, ImageDraw, ImageFilter, ImageOps
import os
import glob
import cv2

#directory where the square mondrian patterns are saved and the resulting images will be saved
Squares_dir = '/Users/niyatee/Documents/PHD/Global-local attention/Stim_code_modified/Global Squares'
files2_dir = '/Users/niyatee/Documents/PHD/Global-local attention/Stim_code_modified/Trash' #for trial and error to decide dimensions required
files = glob.glob(os.path.join(Squares_dir, '*png'))

#for all images in the folder
for f in files:
    Squares = Image.open(f)
    #crop as a square
    Squares_crop = Squares.crop((650,400,1000,750)) #adjust dimensions based on trial and error and the results
    Squares_with_border = ImageOps.expand(Squares_crop,border=5,fill='black')
    ftitle, fext = os.path.splitext(os.path.basename(f))
    Squares_with_border.save(os.path.join(files2_dir, ftitle + '_squaremask' + fext), quality=100)

#directory where the circle mondrian patterns are saved
Circles_dir = '/Users/niyatee/Documents/PHD/Global-local attention/Stim_code_modified/Global Circles'
files1= glob.glob(os.path.join(Circles_dir, '*png'))

#define a circle mask
def mask_circle_transparent(pil_img, blur_radius, offset=0):
    offset = blur_radius * 2 + offset
    mask = Image.new("L", pil_img.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((offset, offset, pil_img.size[0] - offset, pil_img.size[1] - offset), fill=255)
    mask = mask.filter(ImageFilter.SMOOTH)

    result = pil_img.copy()
    result.putalpha(mask)

    return result

#first do a square mask and then crop it into a circle and save
for f in files1:
    Circles =  Image.open(f)
    Square_crop = Circles.crop((650,400,1000,750))
    Circle_mask = mask_circle_transparent(Square_crop, 4)
    ftitle, fext = os.path.splitext(os.path.basename(f))
    Circle_mask.save(os.path.join(files2_dir, ftitle + '_circlemask' + fext), quality=100)




