from tkinter import filedialog
from tkinter import *
from setuptools import Command
from imageresize import resize_image
import sys

# def changeMBText(event):
  # print(minV.get())
  # print(str((int(minV.get())/1000000))+' MB')
  # lblMbS.config(text=str((int(minV.get())/1000000))+' MB')
  # lblMbS.update()

def submit():
  changeStateText('Resizing...')
  ret = resize_image(folder_path.get(), int(perV.get()), float(minV.get()),delV.get())
  if ret:
    changeStateText('Done !')
    
     
def changeStateText(txt):
  lblComp.config(text=txt)
  lblComp.update()
    

def browse():
  # Allow user to select a directory and store it in global var
  # called folder_path
  global folder_path
  filename = filedialog.askdirectory()
  folder_path.set(filename)
    
 
window = Tk()
window.title("Resize Images")
window.geometry('400x300')
window.resizable(0, 0)
folder_path = StringVar()
perV=StringVar()
minV=StringVar()
mbV=StringVar()
delV=BooleanVar()
perV.set(70)
minV.set(2)
lblPer = Label(window,text= 'Percentage :')
lblPer.place(x=10,y=10)
txtPer = Entry(window,width=4 ,textvariable=perV )
txtPer.place(x=90, y=10)
lblMin = Label(window,text= 'Min Size :')
lblMin.place(x=135,y=10)
txtMin = Entry(window, width=4 ,textvariable= minV)
txtMin.place(x=195, y=10)
lblMb = Label(window,text= 'MB')
lblMb.place(x=220,y=10)
lblFolder = Label(window,text='Folder :' )
lblFolder.place(x=10,y=40)
lblComp = Label(window,text='Select a directory')
lblComp.place(x=150,y=120)
txtFolder = Entry(window,textvariable=folder_path, width=40)
txtFolder.place(x=60,y=40)
chkDelete = Checkbutton(window, fg='red', text="Delete Original", variable= delV)
chkDelete.place(x=10,y=70)
btnFolder = Button(window,text="Browse", command=browse)
btnFolder.place(x=315,y=37)
btnRun = Button(window,text="Resize", command=submit)
btnRun.place(x=180,y=80)
btnExit = Button(window,text="Exit", command=sys.exit)
btnExit.place(x=170,y=200)
window.mainloop()










