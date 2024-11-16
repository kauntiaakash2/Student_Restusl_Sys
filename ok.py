#--------------------------Create Function For Submit button------------------#
def Connectdb():
    #------------------UI FOR STUDENT MANAGEMENT-------------------------#
    dbroot = Toplevel()
    dbroot.grab_set()
    dbroot.title('Student Management System')
    dbroot.config(bg='darkseagreen4')
    dbroot.geometry('1174x700+400+200')
    dbroot.iconbitmap('Student.ico')
    dbroot.resizable(False,False)
    #----------------------Creating Frames For UI----------------------------------#
    DataEntryFrame = Frame(dbroot,bg='darkseagreen',relief=GROOVE,borderwidth=5)
    DataEntryFrame.place(x=10,y=80,width=500,height=600)
    #_________________________DATA MENU FRAMES_____________________________________#

    #-----------------------WELCOME MESSAGE----------------------------------#
    frontlabel=Label(DataEntryFrame,text='--------------WELCOME--------------',width=30,font=('arial',22,'italic bold'),bg='darkseagreen')
    frontlabel.pack(side=TOP,expand=True)

    addbtn=Button(DataEntryFrame,text='1.ADD STUDENT DATA',width=25,font=('arial',20,'bold'),bd=6,bg='#FCE6C9',activebackground='#CD1076',activeforeground='#E0EEEE')
    addbtn.pack(side=TOP,expand=True)

    addbtn2=Button(DataEntryFrame,text="2.SEARCH STUDENT DATA",width=25,font=('arial',20,'bold'),bd=6,bg='#FCE6C9',activebackground='#CD1076',activeforeground='#E0EEEE')
    addbtn2.pack(side=TOP,expand=True)

    addbtn3 = Button(DataEntryFrame, text="3.DELETE STUDENT DATA", width=25, font=('arial', 20, 'bold'), bd=6,
                     bg='#FCE6C9', activebackground='#CD1076', activeforeground='#E0EEEE')
    addbtn3.pack(side=TOP, expand=True)

    addbtn4 = Button(DataEntryFrame, text="4.UPDATE STUDENT DATA", width=25, font=('arial', 20, 'bold'), bd=6,
                     bg='#FCE6C9', activebackground='#CD1076', activeforeground='#E0EEEE')
    addbtn4.pack(side=TOP, expand=True)

    addbtn5 = Button(DataEntryFrame, text="5.SHOW COMPLETE DATA", width=25, font=('arial', 20, 'bold'), bd=6,
                     bg='#FCE6C9', activebackground='#CD1076', activeforeground='#E0EEEE')
    addbtn5.pack(side=TOP, expand=True)

    addbtn6 = Button(DataEntryFrame, text="6.EXPORT STUDENT DATA", width=25, font=('arial', 20, 'bold'), bd=6,
                     bg='#FCE6C9', activebackground='#CD1076', activeforeground='#E0EEEE')
    addbtn6.pack(side=TOP, expand=True)

    addbtn7 = Button(DataEntryFrame, text="7.EXIT", width=25, font=('arial', 20, 'bold'), bd=6,
                     bg='#FCE6C9', activebackground='#CD1076', activeforeground='#E0EEEE')
    addbtn7.pack(side=TOP, expand=True)


    #-----------------------------SHOW DATABASE FRAME-----------------------------#
    ShowDataFrame = Frame(dbroot,bg='darkseagreen2',relief=GROOVE,borderwidth=5)
    ShowDataFrame.place(x=544,y=80,width=620,height=600)
    ###################################################################################################
    # -----------------------------STUD MANAGEMENT COLOR CHANGING----------------------------------#
    # ----------HOLD FOR TIME BEING----------------------------------#
    import random
    colors = ["red", "green", "blue", "darkgreen", "deeppink3", "red2", "dodgerblue4"]

    def IntroLabelColorTick():
        fg = random.choice(colors)
        SliderLabel.config(fg=fg)
        SliderLabel.after(100,IntroLabelColorTick)

    '''def IntroLabelTick():
        global count,text
        if (count >= len(ss)):
            count = -1
            text = ''
            SliderLabel.config(text=text)
        else:
            text = text + ss[count]
            SliderLabel.config(text=text)
        count += 1
        SliderLabel.after(200, IntroLabelTick)'''
    # ----------HOLD FOR TIME BEING ENDING LINE----------------------------------#
    ################################################################################################
    #---------------------FLASH STUD MANAGEMENT--------------------#
    ss = " STUDENT MANAGEMENT SYSTEM "
    #count = 0#----------HOLD FOR TIME BEING----------------------------------#
    #text = ''#----------HOLD FOR TIME BEING----------------------------------#
    SliderLabel = Label(dbroot, text=ss, font=('lucida sans typewriter', 25, 'italic bold'), relief=RIDGE, borderwidth=4, width=26,bg='#8FBC8F')
    SliderLabel.place(x=280, y=0)
    #IntroLabelTick()#----------HOLD FOR TIME BEING----------------------------------#
    IntroLabelColorTick()#----------HOLD FOR TIME BEING----------------------------------#
    # --------------------------Clock tick tick on Student Management Page-------------#
    def tick():
        time_string = time.strftime("%H:%M:%S")
        date_string = time.strftime("%d/%m/%Y")
        clock.config(text='Date :' + date_string + "\n" + "Time :" + time_string)
        clock.after(200, tick)

    #---------------------------------------------Clock-------------------------------------------------------#
    clock = Label(dbroot, font=('times', 14, 'bold'), relief=RIDGE, borderwidth=4, width=15, bg='lawn green')
    clock.place(x=0, y=0)
    tick()
    #------------------------Making Action For SUBMIT HOST BUTTON UNDER DATABASE MANAGEMENT-----------------------------------#
    def Connectdb1():
        dbroot1 = Toplevel()
        dbroot1.title('DATABASE CONNECTION')
        dbroot1.grab_set()
        dbroot1.geometry('470x250+800+230')
        dbroot1.iconbitmap('database.ico')
        dbroot1.resizable(False, False)
        dbroot1.config(bg='blue')
        # ________Connectdb Lable_________#
        hostlabel = Label(dbroot1, text="Enter Host :", bg="gold2", font=("times", 20, "bold"), relief=GROOVE,
                      borderwidth=3, width=12, anchor="w")
        hostlabel.place(x=10, y=10)

        adminlabel = Label(dbroot1, text="Enter User :", bg="gold2", font=("times", 20, "bold"), relief=GROOVE,
                      borderwidth=3, width=12, anchor="w")
        adminlabel.place(x=10, y=70)

        passwordlabel = Label(dbroot1, text="Enter Password :", bg="gold2", font=("times", 20, "bold"), relief=GROOVE,
                          borderwidth=3, width=12, anchor="w")
        passwordlabel.place(x=10, y=130)

        # ______________Connectdb Entry______________#
        hostval = StringVar()
        adminval = StringVar()
        passwordtval = StringVar()

        hostentry = Entry(dbroot1, font=('roman', 15, 'bold'), bd=5, textvariable=hostval)
        hostentry.place(x=250, y=10)

        adminentry = Entry(dbroot1, font=('roman', 15, 'bold'), bd=5, textvariable=adminval)
        adminentry.place(x=250, y=70)

        passwordentry = Entry(dbroot1, font=('roman', 15, 'bold'), bd=5, textvariable=passwordtval)
        passwordentry.place(x=250, y=130)

        # _________________Connectdb Button______________#
        submitbutton = Button(dbroot1, text="Submit", font=("roman", 15, "bold"), bd=5, bg='red', width=20,
                          activebackground='blue', activeforeground='white')
        submitbutton.place(x=150, y=190)

        dbroot1.mainloop()

    ######################Connect TO Database########################
    connectbutton = Button(dbroot, text='Connect To Database',width=19, font=('Aptos Narrow',14 ,'bold'),
                           relief=RIDGE, borderwidth=4, bg='aquamarine4',
                           activebackground='blue', activeforeground='white', command=Connectdb1)
    connectbutton.place(x=930, y=0)
    dbroot.mainloop()
######################################|>####################################################################################################
######################################|  >#################################################################################################
######################################|    >################################################################################################
######################################|    >################################################################################################
######################################|    >################################################################################################
######################################|   >################################################################################################
######################################|  >################################################################################################
######################################|>################################################################################################
from tkinter import *
from tkinter import Toplevel
import time
#-----------LOGIN--------------#
root = Tk()
root.title('LOGIN')
root.config(bg='cornsilk3')
root.geometry('400x400+800+350')
root.iconbitmap('aa.ico')
root.resizable(False,False)
#---------LOGIN MESSAGE--------#
m='LOGIN'
LoginLabel=Label(root,text=m,font=('Gumball',50,'bold'),relief=GROOVE,fg='brown2',bg='cornsilk1')
LoginLabel.place(x=94,y=20)
#---------ID & PASSWORD--------#
userlabel = Label(root,text="User Name :",bg="cornsilk3",font=("times",20,"bold"),borderwidth=3,width=10,anchor="w")
userlabel.place(x=10,y=140)

passlabel = Label(root,text="Password :",bg="cornsilk3",font=("times",20,"bold"),borderwidth=3,width=10,anchor="w")
passlabel.place(x=10,y=200)

userval = StringVar()
passtval = StringVar()

userentry = Entry(root, font=('roman', 15, 'bold'), textvariable=userval)
userentry.place(x=170, y=148)

passentry = Entry(root, font=('roman', 15, 'bold'),textvariable=passtval)
passentry.place(x=170, y=208)

#------------SUBMIT BUTTON----------#
submitbutton = Button(root, text="Submit", font=("roman", 15, "bold"), bd=5, bg='red', width=20,
                      activebackground='forestgreen',activeforeground='white',command=Connectdb)
submitbutton.place(x=97, y=300)

root.mainloop()
