import glob
from PIL import Image;
import os,shutil


images_list =('jpeg','JPEG', 'png','PNG', 'jpg','JPG','tif','TIF')
movies_list =('mp4','MP4', 'avi','AVI', '3gp','3GP')

def sizeCalc(percentage, imgSize):
    width  = int(imgSize[0] * percentage/100)
    height = int(imgSize[1] * percentage/100)
    iSize = width, height
    return iSize
 

def image_process(dirpath,output_dir,min_size, percentage,del_original):
  images = [file for file in os.listdir(dirpath) if file.endswith(images_list)]
  movies = [file for file in os.listdir(dirpath) if file.endswith(movies_list)]
  print('-- Processing: ' + dirpath + ' --')
  if not del_original:
      output_dir += "resized/"
  if not os.path.exists(output_dir):
    os.makedirs(output_dir,exist_ok=True)
  for image in images:
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
        if not del_original:
          shutil.copy(fullfile, output_dir)
          print('Just Copied: ',image)
      
  if not del_original:    
    for infile in movies:
      shutil.copy(dirpath + infile, output_dir)
      print('Just Copied: ',infile)  
 

def resize_image(input_dir, percentage=70 , min_size=2 ,del_original=False,scanSub=False):
  min_size= int(min_size * 1000000)
  if scanSub:
    dirpaths = [dirpath for dirpath,dirs,files in os.walk(input_dir) if not dirpath.endswith(('resized'))]
    dirpaths = [dp.replace('\\', '/') for dp in dirpaths]
    for dirpath in dirpaths:
       dirpath = dirpath + "/"
       output_dir = dirpath
       image_process(dirpath, output_dir, min_size, percentage, del_original)
  else:
    dirpath = input_dir + "/"
    output_dir = dirpath
    image_process(dirpath, output_dir, min_size, percentage, del_original)     

  print('-- Done! --')      
  return True



if __name__ == "__main__":
  input_dir = input("Enter the directory path: ")
  percentage = int(input("Enter the percentage: "))
  min_size = int(input("Enter the minimum size in MB: "))
  del_original = input("Delete original files? (y/n): ")
  if del_original == 'y':
    del_original = True
  else:
    del_original = False
  scanSub = input("Scan subfolders? (y/n): ")
  if scanSub == 'y':
    scanSub = True
  else:
    scanSub = False
  resize_image(input_dir, percentage, min_size, del_original,scanSub)
