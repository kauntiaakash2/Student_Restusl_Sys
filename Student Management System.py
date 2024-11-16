#----------------Create Function For Submit Button-------------------#
def submitdb():
    #---------------------UI FOR STUDENT MANAGEMENT SYSTEM-------------------------#
    dbroot = Toplevel()
    dbroot.title('Student Management System')
    dbroot.grab_set()
    dbroot.iconbitmap('SMS.ico')
    dbroot.geometry('1174x700+400+200')
    dbroot.config(bg='#5F9EA0')
    dbroot.resizable(False,False)

    #--------------FRAMES UI---------------------------#
    Dataentryframe=Frame(dbroot,bg='#7AC5CD',relief=RAISED,borderwidth=5)
    Dataentryframe.place(x=10,y=80,width=500,height=600)

    Showdataframe = Frame(dbroot, bg='#7AC5CD', relief=RAISED, borderwidth=5)
    Showdataframe.place(x=544, y=80, width=620, height=600)

    #-------------FLASH STUDENT MANAGEMENT------------------------#
    import random
    colors=['red','green','blue','darkgreen','deeppink3','red2','dodgerblue4']
    def colorflash():
        fg=random.choice(colors)
        sliderlabel.config(fg=fg)
        sliderlabel.after(100,colorflash)
    #-------------------TEXT OF HEADING---------------------------#
    ss='STUDENT MANAGEMENT SYSTEM'
    sliderlabel=Label(dbroot,text=ss,font=('lucida sans typewriter',25,'italic bold'),relief=SUNKEN,borderwidth=4,width=26,bg='#79CDCD')
    sliderlabel.place(x=280,y=0)
    colorflash()
    #---------------------------TICK-TICK--------------------------#
    def tick():
        time_string=time.strftime('%H:%M:%S')
        date_string=time.strftime('%d/%m/%y')
        clock.config(text='Date:'+time_string+'\n'+'Time:'+date_string)
    #-------------------CLOCK------------------------------------#
    clock=Label(dbroot,font=('times',14,'bold'),relief=SUNKEN,borderwidth=4,width=15,bg='#7FFF00')
    clock.place(x=0,y=0)
    tick()
    #------------------------DATABASE CONNECTION WINDOW-------------------#
    def databasedb():
        dbroot1=Toplevel()
        dbroot1.grab_set()
        dbroot1.title('DATABASE CONNECTION')
        dbroot1.geometry('470x250+720+450')
        dbroot1.mainloop()

     #------------------CONNECT TO DATABASE----------------------------#
    databasebutton=Button(dbroot,text='CONNECT TO DATABASE',width=20,font=('Aptos Narrow',14,'bold'),relief=RAISED,bg='#53868B',activebackground='forestgreen',activeforeground='white',command=databasedb)
    databasebutton.place(x=920,y=0)
    dbroot.mainloop()
#####################   #################################################################################
from tkinter import *
from tkinter import Toplevel
import time
#----------LOGIN------------------#
root = Tk()
root.title('LOGIN WINDOW')
root.config(bg='#79CDCD')
root.geometry("400x400+800+350")
root.iconbitmap('aa.ico')
root.resizable(False,False)
#----------LOGIN MESSAGE---------------#
m='LOGIN'
loginlabel=Label(root,text=m,font=('Bahnschrift SemiLight SemiConde',50),relief=GROOVE,bg='#528B8B')
loginlabel.place(x=115,y=20)
#---------ID & PASSWORD----------------#
userlabel=Label(root,text='User Name:',font=('times',20,'bold'),bg='#79CDCD',borderwidth=3,width=10
                ,anchor='w')
userlabel.place(x=10,y=140)

passlabel=Label(root,text='Password:',font=('times',20,'bold'),bg='#79CDCD',borderwidth=3,width=10
                ,anchor="w")
passlabel.place(x=10,y=200)

userval=StringVar()
passval=StringVar()

userentry= Entry(root,font=('roman',15,'bold'),textvariable=userval)
userentry.place(x=170,y=148)

passentry= Entry(root,font=('roman',15,'bold'),textvariable=passval)
passentry.place(x=170,y=208)

#-------------SUBMIT BUTTON-----------------#
submintbutton=Button(root,text="Submit",font=('Ink Free',15,'bold'),bd=5,bg="red",width=20
                     ,activebackground='forestgreen',activeforeground='white',command=submitdb)
submintbutton.place(x=75,y=300)

root.mainloop()