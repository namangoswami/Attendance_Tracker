from tkinter import * 
from tkinter.ttk import *
from tkinter import filedialog
from typing import Text
import pandas as pd

root= Tk()
canvas1 = Canvas(root, width = 856, height = 550)
canvas2=Canvas(root, width = 856, height = 550)
root.title('Attendance Tracker')
def WelcomeScreen():
    canvas2.forget()
    canvas1.pack()
    titleTitle="MS Teams Attendance Tracker "
    canvas1.create_text(400, 30,text=titleTitle, font=('kaushan-script', 30) )
    titleCredit="By Naman and Ankur"
    canvas1.create_text(550, 70,text=titleCredit, font=('kaushan-script', 20) )
    #labelCredit=tk.Label(root, text=titleCredit, fg="black", font=('kaushan-script', 20)).place(x=250, y=50)
    button1 =Button(text='Select File',command=hello)
    canvas1.create_window(50, 215, window=button1)
    button2 = Button(text='Attendance List',command=canvas1.destroy)
    canvas1.create_window(57, 255, window=button2)
    button3 = Button(text='Settings',command=canvas1.destroy)
    canvas1.create_window(50, 295, window=button3)
    button4 =Button(text='About Us',command=canvas1.destroy)
    canvas1.create_window(50, 335, window=button4)
    button5 = Button(text='Exit',command=root.destroy)
    canvas1.create_window(50, 375, window=button5)
    button6 = Button(text='How to Use',command=canvas1.destroy)
    canvas1.create_window(800, 375, window=button6)
def hello ():
    #n=tk.Tk()
    #button1.destroy()
    #n.withdraw()
    file_path=filedialog.askopenfilename()  
    if file_path!='':
        df=pd.read_csv(file_path)
        calc(df)
    canvas1.forget()
    
    #label1 = Label(root, text= df,foreground='black', font=('comic-sans',10))
    
    canvas2.pack()
    canvas2.create_text(400, 200, text=df)
    canvas2.create_text(400, 450, text='Would You like to use this file to mark the attendance?', font=('kaushan-script', 17))
    buttonConfirmYes=Button(text='Yes', command=WelcomeScreen)
    canvas2.create_window(650, 500, window=buttonConfirmYes)
    buttonConfirmNo=Button(text='No', command=WelcomeScreen)
    canvas2.create_window(750, 500, window=buttonConfirmNo)
    #canvas1.create_window( window=label1)
    #label1 = tk.Label(root, text= df, fg='black', font=('comic-sans',10)).place(x=40, y=60)
    #canvas1.create_window( window=label1)
def calc(df):
   # df=df.split()
    for i in df:
        print(i)
WelcomeScreen()
#canvas1.create_window(300, 150, window=button1)

root.mainloop()