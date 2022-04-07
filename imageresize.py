
from PIL import Image;
import PIL;
import sys,os,shutil;
import glob;

def resize_image(input_dir, percentage=50 , max_size=2000000 ,width=None, height=None):
    input_dir = input_dir+'/'
    output_dir = input_dir + "resized/"
    images = [file for file in os.listdir(input_dir) if file.endswith(('jpeg', 'png', 'jpg')) ]
    if not os.path.exists(output_dir):
        os.makedirs(output_dir,exist_ok=True)
    for infile in images: 
        print(infile)
        file, ext = os.path.splitext(infile)
        fullfile = input_dir + infile
        img = Image.open(input_dir + infile)
        if os.path.getsize(fullfile)>max_size:   
           width = int(img.size[0] *percentage/100)
           height = int(img.size[1]*percentage/100)
           size = width, height
           img_resize = img.resize(size,Image.Resampling.NEAREST)
           img_resize.save( output_dir + file  + ext)
        else:
           shutil.copy(fullfile, output_dir)
    return True  



if __name__ == "__main__":
    resize_image(input_dir, percentage)

