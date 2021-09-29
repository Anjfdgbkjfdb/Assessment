from tkinter import *
root = Tk()

receipt_detail = []
total_entry = 0

root.geometry("450x400")

def quit():
    root.destroy()

def save():
    global receipt_detail,Name,Receipt,Item,Qua,total_entry
    receipt_detail.append([Name.get(),Receipt.get(),Item.get(),Qua.get()]) 
    total_entry +=  1
    Name.delete(0,"end")
    Receipt.delete(0,"end")
    Item.delete(0,"end")
    Qua.delete(0,"end")
   
def print():
    global total_entry, row_num
    row_num = 0
    while row_num < total_entry:
        Label(root, text=row_num).grid(column=1,row=row_num+10)
        Label(root, text=(receipt_detail[row_num][0])).grid(column=2,row=row_num+10)
        Label(root, text=(receipt_detail[row_num][1])).grid(column=3,row=row_num+10)
        Label(root, text=(receipt_detail[row_num][2])).grid(column=4,row=row_num+10)
        Label(root, text=(receipt_detail[row_num][3])).grid(column=5,row=row_num+10)
        row_num +=  1

def remove():
    global receipt_detail, delete, total_entry, row_num
    del receipt_detail[int(delete.get())]
    total_entry = total_entry - 1
    Label(root,text="                 ").grid(column=1,row=row_num+9) 
    Label(root,text="                 ").grid(column=2,row=row_num+9) 
    Label(root,text="                 ").grid(column=3,row=row_num+9) 
    Label(root,text="                 ").grid(column=4,row=row_num+9) 
    Label(root,text="                 ").grid(column=5,row=row_num+9)  
    delete.delete(0,"end")
    print()

#below is the code for the buttons of the program and how they are positioned
Button (root, text="Quit", command=quit,width=12).grid(column=5, row=2)
Button (root, text="Append Details", command=save,width=12).grid(column=5, row=4)
Button(root, text="Print Details",command=print,width=12).grid(column=5,row=5)
Button(root,text="Delete Row", command=remove,width=12).grid(column=5, row=7)
#creates spacing between the elements 
Label(root, text="        ").grid(column=1,row=1)
Label(root, text="        ").grid(column=4,row=2)
Label(root, text="        ").grid(column=5,row=6)
Label(root, text="        ").grid(column=5,row=8)
#for the user's input
Label(root, text="Name: ").grid(column=2,row=2,sticky=E)
Name=Entry(root)
Name.grid(column=3, row=2)
Label(root, text="Receipt number: ").grid(column=2,row=3,sticky=E)
Receipt=Entry(root)
Receipt.grid(column=3,row=3)
Label(root, text="Item hired: ").grid(column=2,row=4,sticky=E)
Item=Entry(root)
Item.grid(column=3,row=4)
Label(root, text="Quantity: ").grid(column=2,row=5,sticky=E)
Qua=Entry(root)
Qua.grid(column=3,row=5)
Label(root, text="Row: ").grid(column=2,row=7,sticky=E)
delete=Entry(root)
delete.grid(column=3,row=7)
#headings for the data when user prints data
Label(root, text="Row:").grid(column=1,row=9)
Label(root, text="Name:").grid(column=2,row=9)
Label(root, text="Receipt number:").grid(column=3,row=9)
Label(root, text="Item hired:").grid(column=4,row=9)
Label(root, text="Quantity:").grid(column=5,row=9)

root.mainloop()
