import tkinter as tk
from tkinter import filedialog
import pandas as pd

root= tk.Tk()
canvas1 = tk.Canvas(root, width = 800, height = 600)

canvas1.pack()

def hello ():
    n=tk.Tk()
    #button1.destroy()
    n.withdraw()
    file_path=filedialog.askopenfilename()  
    df=pd.read_excel(file_path)
    label1 = tk.Label(root, text= df, fg='black', font=('comic-sans',10)).place(x=40, y=60)
    #canvas1.create_window( window=label1)
    input('press any key to continue')    

button1 = tk.Button(text='Select Excel File',command=hello)
canvas1.create_window(200, 150, window=button1)

root.mainloop()