import glob
from PIL import Image;
import os,shutil
ext_list =('jpeg','JPEG', 'png','PNG', 'jpg','JPG','tif','TIF')

def resize_image(input_dir, percentage=70 , min_size=2 ,del_original=False):
  min_size= int(min_size * 1000000)
  dirpaths = [dirpath for dirpath,dirs,files in os.walk(input_dir) if not dirpath.endswith(('resized'))]
  for dirpath in dirpaths:
    dirpath=dirpath+"/"
    output_dir = dirpath
    if not del_original:
      output_dir += "resized/"
    images = [file for file in os.listdir(dirpath) if file.endswith(ext_list)]
    for image in images:
      if not os.path.exists(output_dir):
        os.makedirs(output_dir,exist_ok=True)
      file, ext = os.path.splitext(image)
      fullfile = dirpath + image
      img = Image.open(fullfile)
      if os.path.getsize(fullfile) > min_size: 
        imgSize = img.size[0], img.size[1]   # width, height
        newSize = sizeCalc(percentage, imgSize)
        img_resize = img.resize(newSize,Image.Resampling.NEAREST)
        img_resize.save( output_dir + file  + ext)
        print('Resized & Copy: ',image)
      else:
        shutil.copy(fullfile, output_dir)
        print('Just Copied: ',image)
    movies = [file for file in os.listdir(dirpath) if file.endswith(('mp4','MP4', 'avi','AVI', '3gp','3GP')) ]  
    if not del_original:     
      for infile in movies:
        shutil.copy(dirpath + infile, output_dir)
        print('Just Copied: ',infile)  
  print('-- Done! --')      
  return True

def sizeCalc(percentage, imgSize):
    width  = int(imgSize[0] * percentage/100)
    height = int(imgSize[1] * percentage/100)
    iSize = width, height
    return iSize
 