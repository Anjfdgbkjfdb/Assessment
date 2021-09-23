from tkinter import *
root = Tk()

root.geometry("400x400")
def quit():
    root.destroy()

b1 = Button (root, text="Quit", command=quit)
b1.pack() 

def enter():
    Name=e1.get() 
    string="Name = " + Name
    l1["text"]=string

    Receipt=e2.get()
    string="Receipt number = " + Receipt
    l2["text"]=string

    Item=e3.get()
    string="Item hired = " + Item
    l3["text"]=string

    Qua=e4.get()
    string="Quantity = " + Qua
    l4["text"]=string

b1 = Button (root, text="Enter", command=enter)
la = Label(root, text="Name: ")
lb = Label(root, text="Receipt number: ")
lc = Label(root, text="Item hired: ")
ld = Label(root, text="Quantity: ")


e1=Entry(root)
l1=Label(root)

e2=Entry(root)
l2=Label(root)

e3=Entry(root)
l3=Label(root)

e4=Entry(root)
l4=Label(root)

b1.pack()
e1.pack() 
l1.pack()
la.pack()

e2.pack()
l2.pack()
lb.pack()

e3.pack()
l3.pack()
lc.pack()

e4.pack()
l4.pack()
ld.pack()

root.mainloop()
