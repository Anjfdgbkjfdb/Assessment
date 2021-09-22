from tkinter import *
root = Tk()

root.geometry("400x200")

def quit():
    root.destroy()

b1 = Button (root, text="Quit", command=quit)
b1.pack()

root.mainloop()