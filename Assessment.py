from tkinter import *
root = Tk()

receipt_detail = []
total_entry = 0

root.geometry("400x400")
def quit():
    root.destroy()

b1 = Button (root, text="Quit", command=quit)
b1.pack() 

def save():
    global receipt_detail,Name,Receipt,Item,Qua,total_entry

    receipt_detail.append([Name.get(),Receipt.get(),Item.get(),Qua.get()]) 
    total_entry +=  1

def print():
    global total_entry, receipt_detail,Name,Receipt,Item,Qua
    string= receipt_detail
    Label(root,text = string).pack()

Button (root, text="Append Details", command=save).pack()
Label(root, text="Name: ").pack()
Label(root, text="Receipt number: ").pack()
Label(root, text="Item hired: ").pack()
Label(root, text="Quantity: ").pack()
Button(root, text="Print Details",command=print,width = 10) .pack()

Name=Entry(root)
Name.pack()
Receipt=Entry(root)
Receipt.pack()
Item=Entry(root)
Item.pack()
Qua=Entry(root)
Qua.pack()

root.mainloop()
