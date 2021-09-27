from tkinter import *
root = Tk()

receipt_detail = []
total_entry = 0

root.geometry("400x400")

def quit():
    root.destroy()

def save():
    global receipt_detail,Name,Receipt,Item,Qua,total_entry

    receipt_detail.append([Name.get(),Receipt.get(),Item.get(),Qua.get()]) 
    total_entry +=  1

def print():
    global total_entry, row_num
    row_num = 0
    while row_num < total_entry :
        Label(root, text=row_num).grid(column=1,row=row_num+8) 
        Label(root, text=(receipt_detail[row_num][0])).grid(column=2,row=row_num+8)
        Label(root, text=(receipt_detail[row_num][1])).grid(column=3,row=row_num+8)
        Label(root, text=(receipt_detail[row_num][2])).grid(column=4,row=row_num+8)
        Label(root, text=(receipt_detail[row_num][3])).grid(column=5,row=row_num+8)
        row_num +=  1

Button (root, text="Quit", command=quit).grid(column=5, row=2)
Button (root, text="Append Details", command=save).grid(column=5, row=4)
Button(root, text="Print Details",command=print,width = 10).grid(column=5,row=5)
Label(root, text="        ").grid(column=1,row=1)
Label(root, text="        ").grid(column=4,row=2)

Label(root, text="Name: ").grid(column=2,row=2)
Name=Entry(root)
Name.grid(column=3, row=2)
Label(root, text="Receipt number: ").grid(column=2,row=3)
Receipt=Entry(root)
Receipt.grid(column=3,row=3)
Label(root, text="Item hired: ").grid(column=2,row=4)
Item=Entry(root)
Item.grid(column=3,row=4)
Label(root, text="Quantity: ").grid(column=2,row=5)
Qua=Entry(root)
Qua.grid(column=3,row=5)

root.mainloop()
