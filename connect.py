def Connectdb():
    dbroot = Toplevel()
    dbroot.grab_set()
    dbroot.geometry('470x250+800+230')
    dbroot.resizable(False,False)
    dbroot.config(bg='blue')
    #________Connectdb Lable_________#
    hostlabel = Label(dbroot,text="Enter Host :",bg="gold2",font=("times",20,"bold"),relief=GROOVE,borderwidth=3,width=12,anchor="w")
    hostlabel.place(x=10,y=10)

    userlabel = Label(dbroot, text="Enter User :", bg="gold2", font=("times", 20, "bold"), relief=GROOVE, borderwidth=3,width=12, anchor="w")
    userlabel.place(x=10, y=70)

    passwordlabel = Label(dbroot, text="Enter Password :", bg="gold2", font=("times", 20, "bold"), relief=GROOVE, borderwidth=3,width=12, anchor="w")
    passwordlabel.place(x=10, y=130)

    #______________Connectdb Entry______________#
    hostval = StringVar()
    userval = StringVar()
    passwordtval = StringVar()

    hostentry = Entry(dbroot,font=('roman', 15, 'bold'), bd=5, textvariable=hostval)
    hostentry.place(x=250,y=10)

    userentry = Entry(dbroot, font=('roman', 15, 'bold'), bd=5, textvariable=userval)
    userentry.place(x=250, y=70)

    passwordentry = Entry(dbroot, font=('roman', 15, 'bold'), bd=5,textvariable=passwordtval)
    passwordentry.place(x=250, y=130)

    #_________________Connectdb Button______________#
    submitbutton= Button(dbroot,text="Submit",font=("roman",15,"bold"),bd=5,bg='red',width=20,activebackground='blue',activeforeground='white')
    submitbutton.place(x=150,y=190)

    dbroot.mainloop()

######################################################
def tick():
    time_string = time.strftime("%H:%M:%S")
    date_string = time.strftime("%d/%m/%Y")
    clock.config(text='Date :'+date_string+"\n"+"Time :"+time_string)
    clock.after(200,tick)
##################INTRO Slider################
import random
colors = ["red","green","blue","darkgreen","deeppink3","red2","dodgerblue4"]
def IntroLabelColorTick():
    fg = random.choice(colors)
    SliderLabel.config(fg=fg)
    SliderLabel.after(100,IntroLabelColorTick)
def IntroLabelTick():
    global count,text
    if (count>=len(ss)):
        count=-1
        text=''
        SliderLabel.config(text=text)
    else:
        text=text+ss[count]
        SliderLabel.config(text=text)
    count += 1
    SliderLabel.after(200,IntroLabelTick)
##########################################################
from tkinter import *
from tkinter import Toplevel
import time

root = Tk()
root.title('Student Management System')
root.config(bg='darkseagreen4')
root.geometry('1174x700+200+50')
root.iconbitmap()
root.resizable(False,False)
############################frames################
DataEntryFrame = Frame(root,bg='darkseagreen',relief=GROOVE,borderwidth=5)
DataEntryFrame.place(x=10,y=80,width=500,height=600)

DataEntryFrame = Frame(root,bg='darkseagreen2',relief=GROOVE,borderwidth=5)
DataEntryFrame.place(x=544,y=80,width=620,height=600)
##################slider################
ss="WELCOME TO STUDENT MANAGENENT SYSTEM"
count=0
text=''
##########################################################
SliderLabel = Label(root,text=ss,font=('chiller',30,'italic bold'),relief=RIDGE,borderwidth=4,width=35,bg='cyan')
SliderLabel.place(x=260,y=0)
IntroLabelTick()
IntroLabelColorTick()
########################Clock########################
clock =Label(root,font=('times',14,'bold'),relief=RIDGE,borderwidth=4,width=15,bg='lawn green')
clock.place(x=0,y=0)
tick()
######################Connect TO Database########################
connectbutton = Button(root,text='Connect To Database',width=23,font=('chiller',19,'italic bold'),relief=RIDGE,borderwidth=4,bg='aquamarine4',
                       activebackground='blue',activeforeground='white',command=Connectdb)
connectbutton.place(x=930,y=0)
root.mainloop()