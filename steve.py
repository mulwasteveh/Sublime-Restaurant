from tkinter import *
from PIL import ImageFile
window = Tk()
window.title("Steveh")
window.geometry("500x500")
window.configure(background="cadet blue")


def calculate():
    Chapati = e1.get()
    Mandazi = e2.get()
    Ndengu = e3.get()
    Beans = e4.get()
    Cake = e5.get()
    print(type(Cake))
    total = ((int(Chapati)*20)+(int(Mandazi)*10)+(int(Ndengu)*15)+(int(Beans)*15)+(int(Cake)*5))

    label14 = Label(window, text=total, font="times 18 bold")
    label14.place(x=150, y=430)


label7=Label(window, text="STEVE'S RESTAURANT",font="times 28 bold")
label7.place(x=70, y=20)
label7.anchor = "center"

label1=Label(window, text="MENU",font="times 28 bold")
label1.place(x=350,y=80)

label2=Label(window, text="Chapati      @ 20",font="times 18")
label2.place(x=300,y=130)

label3=Label(window, text="Mandazi      @ 10",font="times 18")
label3.place(x=300,y=180)

label4=Label(window, text="Ndengu        @ 15",font="times 18")
label4.place(x=300,y=230)

label5=Label(window, text="Beans        @ 15",font="times 18")
label5.place(x=300,y=280)

label6=Label(window, text="Cake        @ 5",font="times 18")
label6.place(x=300,y=330)

#--------x-----Billing section---------x-------------
label8 = Label(window, text="Select your items",font="times 18 bold")
label8.place(x=20,y=80)

label9 = Label(window, text="Chapati",font="times 18")
label9.place(x=25,y=120)
e1 = Entry(window)
e1.place(x=25,y=150)

label10 = Label(window, text="Mandazi",font="times 18")
label10.place(x=25,y=170)
e2 = Entry(window)
e2.place(x=25,y=200)

label11 = Label(window, text="Ndengu",font="times 18")
label11.place(x=25,y=220)
e3 = Entry(window)
e3.place(x=25,y=250)

label12 = Label(window, text="Beans",font="times 18")
label12.place(x=25,y=270)
e4 = Entry(window)
e4.place(x=25,y=300)

label13 = Label(window, text="Cake",font="times 18")
label13.place(x=25,y=320)
e5 = Entry(window)
e5.place(x=25,y=350)

b2 = Button(window, text="Bill",width=15, font="times 15 bold", command=calculate)
b2.place(x=150, y=380)


def Print():
    print("This is all what you ate")
    a = e2.get()
    a = a.split(",")
    for i in a:
        print(i)
        print("Thanks")


b3 = Button(window, text="Print receipt", font="times 15 bold", command=Print)
b3.place(x=350, y=380)

window.mainloop()