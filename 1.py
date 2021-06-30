from tkinter import *
window=Tk()
window.geometry("2000x1000")

def calculate():
    Dosa=e1.get()
    Poha=e2.get()
    Shabudana=e3.get()
    Samosa=e4.get()
    Idli_sambar=e5.get()
    Kachori=e6.get()
    Dabeli=e7.get()
    Upma=e8.get()
    Vada_pav=e9.get()
    Cofee=e10.get()
    Tea=e11.get()
    Jalebi_fafda=e12.get()
    Dhokla=e13.get()
    Kanda_bhaji=e14.get()
    Mung_bhaji=e15.get()
    Wada_sambar=e16.get()

    total=(int(Dosa)*35+int(Poha)*35+int(Shabudana)*40+int(Samosa)*10+int(Idli_sambar)*40+int(Kachori)*10+int(Dabeli)*20+int(Upma)*30+int(Vada_pav)*10+int(Cofee)*10+int(Tea)*10
           +int(Jalebi_fafda)*40+int(Dhokla)*40+int(Kanda_bhaji)*30+int(Mung_bhaji)*40+int(Wada_sambar)*40)
    label24 = Label(window, text=total, font="times 18 bold")
    label24.place(x=540, y=660)

    label25 = Label(window, text="Total-", font=("times new roman",20,"bold"))
    label25.place(x=450, y=660)

    label26 = Label(window, text="Rs", font="times 18 bold")
    label26.place(x=685, y=660)








Menu=Frame(window,bd=4,relief=RIDGE)
Menu.place(x=535,y=653,width=150,height=42)

label1=Label(window,text="Annapurna Break fast center",bd=10,relief=GROOVE,font=("times new roman",30,"bold"),bg="yellow",fg="red")
label1.pack(side=TOP,fill=X)


#----------------menu section----------

Menu=Frame(window,bd=4,relief=RIDGE)
Menu.place(x=400,y=90,width=400,height=520)




label2=Label(window,text="Menu",font="times 28 bold")
label2.place(x=550,y=70)

label3=Label(window,text="Dosa                         35 Rs",font="times 16 bold")
label3.place(x=450,y=120)

label4=Label(window,text="Poha                         35 Rs",font="times 16 bold")
label4.place(x=450,y=150)


label5=Label(window,text="Shabudna                40 Rs",font="times 16 bold")
label5.place(x=450,y=180)


label6=Label(window,text="Samosa                    10 Rs",font="times 16 bold")
label6.place(x=450,y=210)

label7=Label(window,text="Idli Sambar             40 Rs",font="times 16 bold")
label7.place(x=450,y=240)

label8=Label(window,text="Kachori                   10 Rs",font="times 16 bold")
label8.place(x=450,y=270)

label9=Label(window,text="Dabeli                      20 Rs",font="times 16 bold")
label9.place(x=450,y=300)

label10=Label(window,text="Upma                       30 Rs",font="times 16 bold")
label10.place(x=450,y=330)

label11=Label(window,text="Vada Pav                10 Rs",font="times 16 bold")
label11.place(x=450,y=360)

label12=Label(window,text="Cofee                       10 Rs",font="times 16 bold")
label12.place(x=450,y=390)

label13=Label(window,text="Tea                           10 Rs",font="times 16 bold")
label13.place(x=450,y=420)

label14=Label(window,text="Fafda jalebi            40 Rs",font="times 16 bold")
label14.place(x=450,y=450)

label15=Label(window,text="Dhokla                     40 Rs",font="times 16 bold")
label15.place(x=450,y=480)

label16=Label(window,text="Kanda Bhaji           30 Rs",font="times 16 bold")
label16.place(x=450,y=510)

label18=Label(window,text="Mung Bhaji             40 Rs",font="times 16 bold")
label18.place(x=450,y=540)

label19=Label(window,text="Vada Sambar         40 Rs",font="times 16 bold")
label19.place(x=450,y=570)




#-------------billing section----------------


Menu=Frame(window,bd=4,relief=RIDGE,bg="Light Blue")
Menu.place(x=10,y=70,width=380,height=500)


label7=Label(window,text="Select The Items",bg="Light Blue",fg="black",font=("times new roman",18,"bold"))
label7.place(x=90,y=90)

label8=Label(window,text="Dosa",bg="Light Blue",fg="black",font=("times new roman",18,"bold"))
label8.place(x=20,y=120)

e1=Entry(window)
e1.insert(0,"0")
e1.place(x=20,y=150)

label9=Label(window,text="Poha",bg="Light Blue",fg="black",font=("times new roman",18,"bold"))
label9.place(x=250,y=120)

e2=Entry(window)
e2.insert(0,"0")
e2.place(x=250,y=150)

label10=Label(window,text="Shabudana",bg="Light Blue",fg="black",font=("times new roman",18,"bold"))
label10.place(x=20,y=200)

e3=Entry(window)
e3.insert(0,"0")
e3.place(x=20,y=230)

label11=Label(window,text="Samosa",bg="Light Blue",fg="black",font=("times new roman",18,"bold"))
label11.place(x=250,y=200)

e4=Entry(window)
e4.insert(0,"0")
e4.place(x=250,y=230)

label12=Label(window,text="Idli Sambar",bg="Light Blue",fg="black",font=("times new roman",18,"bold"))
label12.place(x=20,y=280)

e5=Entry(window)
e5.insert(0,"0")
e5.place(x=20,y=310)

label13=Label(window,text="Kachori",bg="Light Blue",fg="black",font=("times new roman",18,"bold"))
label13.place(x=250,y=280)

e6=Entry(window)
e6.insert(0,"0")
e6.place(x=250,y=310)

label14=Label(window,text="Dabeli",bg="Light Blue",fg="black",font=("times new roman",18,"bold"))
label14.place(x=20,y=360)

e7=Entry(window)
e7.insert(0,"0")
e7.place(x=20,y=390)

label15=Label(window,text="Upma",bg="Light Blue",fg="black",font=("times new roman",18,"bold"))
label15.place(x=250,y=360)

e8=Entry(window)
e8.insert(0,"0")
e8.place(x=250,y=390)




Menu=Frame(window,bd=4,relief=RIDGE,bg="Light Blue")
Menu.place(x=810,y=70,width=400,height=500)

label26=Label(window,text="Select The Items",bg="Light Blue",fg="black",font=("times new roman",18,"bold"))
label26.place(x=900,y=90)

label16=Label(window,text="Vada Pav",bg="Light Blue",fg="black",font=("times new roman",18,"bold"))
label16.place(x=820,y=120)

e9=Entry(window)
e9.insert(0,"0")
e9.place(x=820,y=150)

label17=Label(window,text="Cofee",bg="Light Blue",fg="black",font=("times new roman",18,"bold"))
label17.place(x=1070,y=120)

e10=Entry(window)
e10.insert(0,"0")
e10.place(x=1070,y=150)

label18=Label(window,text="Tea",bg="Light Blue",fg="black",font=("times new bold",18,"bold"))
label18.place(x=820,y=200)

e11=Entry(window)
e11.insert(0,"0")
e11.place(x=820,y=230)

label19=Label(window,text="Jalebi Fafda",bg="Light Blue",fg="black",font=("times new roman",18,"bold"))
label19.place(x=1070,y=200)

e12=Entry(window)
e12.insert(0,"0")
e12.place(x=1070,y=230)

label20=Label(window,text="Dhokla",bg="Light Blue",fg="black",font=("times new roman",18,"bold"))
label20.place(x=820,y=280)

e13=Entry(window)
e13.insert(0,"0")
e13.place(x=820,y=310)

label21=Label(window,text=" Kanda Bhaji",bg="Light Blue",fg="black",font=("times new roman",18,"bold"))
label21.place(x=1060,y=280)

e14=Entry(window)
e14.insert(0,"0")
e14.place(x=1070,y=310)

label22=Label(window,text="Mung Bhaji",bg="Light Blue",fg="black",font=("times new roman",18,"bold"))
label22.place(x=820,y=360)

e15=Entry(window)
e15.insert(0,"0")
e15.place(x=820,y=390)

label23=Label(window,text="Vada Sambar",bg="Light Blue",fg="black",font=("times new roman",18,"bold"))
label23.place(x=1060,y=360)

e16=Entry(window)
e16.insert(0,"0")
e16.place(x=1070,y=390)



b2=Button(window,text="bill",bd=8,bg="yellow",fg="black",width=20,command=calculate)
b2.place(x=530,y=613)
window.mainloop()

