from tkinter import filedialog
from tkinter import *
from imageresize import resize_image

def resizer():
    # Allow user to select a directory and store it in global var
    # called folder_path
    global folder_path
    filename = filedialog.askdirectory()
    folder_path.set(filename)
    ret = resize_image(folder_path.get(), int(txtPer.get()), int(txtMin.get()))
    if ret:
      print('Done!')
      lblComp = Label(window,text='Done !')
     
   


window = Tk()
window.title("Resize Images")
window.geometry('400x300')
window.resizable(0, 0)
folder_path = StringVar()
lblPer = Label(window,text= 'Percentage :')
lblPer.place(x=10,y=10)
txtPer = Entry(window,width=2)
txtPer.place(x=90, y=10)
lblMin = Label(window,text= 'Min Size :')
lblMin.place(x=220,y=10)
txtMin = Entry(window, width=10)
txtMin.place(x=290, y=10)
lblPath = Label(window,text='Path :')
lblPath.place(x=10,y=40)
lblComp = Label(window,text='Select a directory')
lblComp.place(x=150,y=120)
txtPath = Entry(window,textvariable=folder_path, width=50)
txtPath.place(x=70,y=40)
button2 = Button(text="Browse", command=resizer)
button2.place(x=170,y=80)


window.mainloop()



