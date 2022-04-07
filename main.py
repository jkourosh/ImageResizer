from tkinter import filedialog
import subprocess

from tkinter import *
from imageresize import resize_image
import sys
def browse():
    # Allow user to select a directory and store it in global var
    # called folder_path
    global folder_path
    filename = filedialog.askdirectory()
    folder_path.set(filename)
    
     
def submit():
  ret = resize_image(folder_path.get(), int(perV.get()), int(minV.get()))
  openfolder=folder_path.get()+'/resized'
  if ret:
    print('Done!')
    lblComp = Label(window,text='Done !')
    # subprocess.Popen(r'explorer /select,'+'"' openfolder+'"', shell=True)


window = Tk()
window.title("Resize Images")
window.geometry('400x300')
window.resizable(0, 0)
folder_path = StringVar()
perV=StringVar()
minV=StringVar()
perV.set(70)
minV.set(2000000)
lblPer = Label(window,text= 'Percentage :')
lblPer.place(x=10,y=10)
txtPer = Entry(window,width=4 ,textvariable=perV )
txtPer.place(x=90, y=10)
lblMin = Label(window,text= 'Min Size :')
lblMin.place(x=220,y=10)
txtMin = Entry(window, width=10 ,textvariable= minV)
txtMin.place(x=290, y=10)
lblPath = Label(window,text='Path :')
lblPath.place(x=10,y=40)
lblComp = Label(window,text='Select a directory')
lblComp.place(x=150,y=120)
txtPath = Entry(window,textvariable=folder_path, width=50)
txtPath.place(x=70,y=40)
btnPath = Button(text="Browse", command=browse)
btnPath.place(x=170,y=80)
btnRun = Button(text="Resize", command=submit)
btnRun.place(x=250,y=80)
btnExit = Button(text="Exit", command=sys.exit)
btnExit.place(x=170,y=200)


window.mainloop()



