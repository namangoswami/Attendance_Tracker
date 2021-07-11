from tkinter import * 
from tkinter.ttk import *
from tkinter import filedialog
from typing import DefaultDict, Text
import pandas as pd
import pickle
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
        with open(file_path) as df:
            df = df.read()
    calc(df)
    write()
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
class student:
    name=""
    totaltime=0
    lastStatus=0
    lastHour=0
    lastSecond=0
    lastMinute=0
    lastDate=0
    lastMonth=0
    lastYear=0
    timeCodeTemp=0
    present=False
    def __init__(self, name, status, timeHour, timeMinute,  timeSeconds, date, month, year, timeCode):
        self.name=name
        self.totaltime=0
        self.lastStatus=status
        self.lastDate=date
        self.lastMonth=month
        self.lastYear=year
        self.lastHour=timeHour
        self.lastMinute=timeMinute
        self.lastSecond=timeSeconds
        if timeCode=="\x00P\x00M\x00":
            self.timeCodeTemp=1
        else:
            self.timeCodeTemp=0
    def determinePresent(self):
        if self.totaltime>40 or self.totaltime==0:
            self.present=True
        else:
            self.present=False
        return self.present
    def addTime2(self,timeHour, timeMinute, timeSeconds, timeCode, date, month, year):
        self.addTime(timeHour, timeMinute, timeSeconds, timeCode, date, month, year)
        self.lastDate=date
        self.lastMonth=month
        self.lastYear=year
        self.lastHour=timeHour
        self.lastMinute=timeMinute
        self.lastSecond=timeSeconds
    def addTime(self,timeHour, timeMinute, timeSeconds, timeCode, date, month, year):
        if self.lastStatus=='\x00J\x00o\x00i\x00n\x00e\x00d\x00':
            return
        if self.totaltime>720:
            return
        if timeCode=="\x00P\x00M\x00":
            timeTemp=1
        else:
            timeTemp=0
        if self.lastYear>year:
            return
        elif self.lastMonth>month :
            return
        elif self.lastDate>date:
            return
        if timeTemp==1:
            time24H=12*60+timeHour*60+timeMinute+timeSeconds/60
        else:
            time24H=timeHour*60+timeMinute+timeSeconds/60
        if self.timeCodeTemp==1:
            time24HSelf=12*60+self.lastHour*60+self.lastMinute+self.lastSecond/60
        else:
            time24HSelf=self.lastHour*60+self.lastMinute+self.lastSecond/60
        print( self.name, time24H, time24HSelf)
        if self.lastMonth>month:
            self.present=True
            self.totaltime=720
        elif self.lastDate>date+1:
            self.present=True
            self.totaltime=720
            return
        elif self.lastYear>year:
            self.present=True
            self.totaltime=720
            return
        if self.lastDate==date:
            self.totaltime+=(time24H-time24HSelf)
        elif self.lastDate+1==date:
            time24HSelf=1440-time24HSelf
            self.totaltime=time24HSelf+time24H
            if self.totaltime>720:
                self.totaltime=720
                return
    def dispStudent(self):
        print("Name: "+self.name)
       # print("Status: ", self.lastStatus)
       # print("Time: ", timeHour, ":", timeMinute, ":", timeSecond)
        print("Total Time: ", self.totaltime)
        print("Present: ", self.determinePresent())
        #print("Date: ", date, month, year)
class lecture:
    name=""
    students=[]
allStudents=[]
studentMap={}
#studentMap=DefaultDict(lambda: 0, 0)
studentdeclareReg={}
def calc(df):
    print(df)
    df=df.split()
    i=5
    print(df.__len__())

    while i<(df.__len__()):
        print(i)
       # print(df[i])
       # print(i)
        #print(df[i])
        name=df[i]
        i+=1
        #print(df[i])
        newstr='\x00J\x00o\x00i\x00n\x00e\x00d\x00'
        newstr2='\x00L\x00e\x00f\x00t\x00'
        #print(newstr.split())
        #print(newstr2.split())
        while i<df.__len__():
            if len(df[i])==len(newstr):
            #  print("Length Match")
                if df[i]!=newstr:
                    name+=" "+df[i]
                    i+=1
                else:
                    break
                #  print(df[i])
            elif len(df[i])==len(newstr2):
                if df[i]!=newstr2:
                    name+=" "+df[i]
                    i+=1
                else:
                    break
                #  print(df[i])
            else:
                name+=" "+df[i]
                i+=1
        if i>=df.__len__():
            break
        
        status=-1
        statusStr=df[i]
        if df[i]=='Joined':
            status=1
        elif df[i]=='Left':
            status=0
        
        i+=1
        #print(df[i])
        dateTemp=df[i]
        i+=1
        j=0
        # details 
        month=0
        date=0
        year=0
        monthdone=False
        yeardone=False
        datedone=False
      # timing calculate
        while j<len(dateTemp):
           # print(monthdone, datedone)
            if dateTemp[j]!='\x00' :
                if dateTemp[j]=='/':
                    #print(dateTemp[i])
                    if monthdone==False:
                        monthdone=True   
                    elif datedone==False:
                        datedone=True
                elif dateTemp[j]>='0' and dateTemp[j]<='9':
                    #print(dateTemp[j])
                    if monthdone==False:
                        month=month*10+int(dateTemp[j])
                    elif datedone==False:
                        date=date*10+ int(dateTemp[j])
                    else:
                        year=year*10+int(dateTemp[j])
            j+=1
        #print(date) 
        #print(month) 
        #print(year)
      #  print(df[i])
        #i+=1
        timeTemp=df[i]
        beforeColonHour=False
        beforecolonMinute=False
        timeHour=0
        timeMinute=0
        timeSecond=0
        j=0
        while j<len(timeTemp):
            #print(timeTemp[j])
            if timeTemp[j]!='\x00' :
                if timeTemp[j]==':':
                    #print(dateTemp[i])
                    if beforeColonHour==False:
                        beforeColonHour=True
                    else:
                        beforecolonMinute=True
                elif timeTemp[j]>='0' and timeTemp[j]<='9':
                    #print(timeTemp[j])
                    if beforeColonHour==False:
                        timeHour=timeHour*10+int(timeTemp[j])
                    elif beforecolonMinute==False:
                        timeMinute=timeMinute*10+int(timeTemp[j])
                    else:
                        timeSecond=timeSecond*10+int(timeTemp[j])
            j+=1
        i+=1
       
       # print(df[i])
        timeCode=df[i]
       # print(status)
       # for j in dateTemp:
        #print(i)
        i+=1
        tempMapCheck=studentMap.get(name, 0)
        print(tempMapCheck)
        if tempMapCheck==0:
            print("If entered ", name)
            #studentdeclareReg[name]=1
            new=student(name, status, timeHour, timeMinute, timeSecond, date, month, year, timeCode)
            studentMap[name]=new
            allStudents.append(studentMap[name])
            studentMap[name].dispStudent()
        else:
            print("Else entered")
            studentMap[name].addTime2(timeHour, timeMinute, timeSecond, timeCode, date, month, year)
            studentMap[name].dispStudent()
def write():
    with open("temp.txt", "wb") as temp:
        for i in allStudents:
            pickle.dump(i, temp, pickle.HIGHEST_PROTOCOL)
    with open("temp.txt", "rb") as temp:
        while temp:
            try:
                naman=pickle.load(temp)
                naman.dispStudent()
            except (EOFError):
                break
    #file.close()

        
WelcomeScreen()
#canvas1.create_window(300, 150, window=button1) 
root.mainloop()

