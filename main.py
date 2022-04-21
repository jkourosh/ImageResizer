
from tkinter import filedialog
from tkinter import *
from imageresize import resize_image





class ImageResize(Tk):
    def __init__(self, master):
        self.master = master
        self.master.title("Resize Images") 
        self.master.eval('tk::PlaceWindow . center')
        self.master.geometry('400x180')
        self.master.resizable(0, 0)
        self.lblPers = Label(master,text= 'Percentage :')
        self.lblPers.place(x=10,y=10)
        self.txtPer = Entry(master,width=4 ,textvariable=perV )
        self.txtPer.place(x=82, y=10)
        self.lblPer = Label(master,text= '%')
        self.lblPer.place(x=110,y=10)
        self.lblMin = Label(master,text= 'Min Image Size To Be Reduce:')
        self.lblMin.place(x=150,y=10)
        self.txtMin = Entry(master, width=4 ,textvariable= minV)
        self.txtMin.place(x=315, y=10)
        self.lblMb = Label(master,text= 'MB')
        self.lblMb.place(x=340,y=10)
        self.lblFolder = Label(master,text='Folder :' )
        self.lblFolder.place(x=10,y=40)
        self.lblComp = Label(master,text='Select a directory')
        self.lblComp.place(x=150,y=70)
        self.txtFolder = Entry(master,textvariable=folder_path, width=40)
        self.txtFolder.place(x=60,y=40)
        self.chkSub = Checkbutton(master,  text="Scan Subfolder", variable= subV)
        self.chkSub.place(x=10,y=70)
        self.chkDelete = Checkbutton(master, fg='red', text="Delete Original", variable= delV)
        self.chkDelete.place(x=10,y=90)
        self.btnFolder = Button(master,text="Browse", command= self.browse)
        self.btnFolder.place(x=315,y=37)
        self.btnRun = Button(master,text="Resize", command= self.submit)
        self.btnRun.place(x=180,y=95)
        self.btnExit = Button(master,text="Exit", command= master.quit)
        self.btnExit.place(x=183,y=130)
        self.lblVer = Label(master,text= 'V: 1.2')
        self.lblVer.place(x=10,y=140)
     

        
    
    def changeStateText(self,txt):
      self.lblComp.config(text=txt)
      self.lblComp.update()
    
    def submit(self):
      self.changeStateText('Resizing...')
      ret = resize_image(folder_path.get(), int(perV.get()), float(minV.get()),delV.get(),subV.get())
      if ret:
        self.changeStateText('Done !')
        
    def browse(self):
          # Allow user to select a directory and store it in global var
          # called folder_path
      global folder_path
      filename = filedialog.askdirectory()
      folder_path.set(filename)
    
    def greet(self):
        print("Greetings!")



root = Tk()
folder_path = StringVar()
perV=StringVar()
minV=StringVar()
mbV=StringVar()
delV=BooleanVar()
subV=BooleanVar()

perV.set(70)
minV.set(2)

app_gui = ImageResize(root)
root.mainloop()