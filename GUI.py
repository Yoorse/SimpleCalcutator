from tkinter import *

root = Tk()

root.geometry("300x300")

root.title(" Simple Calculator")

w = Label(root, text="choose calculation", font="helvetica", fg="Green")
w.pack()

b1 = Button(root, text="Addition", width=30)
b1.pack()

root.mainloop()




