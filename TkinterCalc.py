from tkinter import  *

root = Tk()
#creating a lable
myLable1 = Label(root, text = "Hello World")
myLable2 = Label(root, text = "How are u?")
#moving it to the screen
myLable1.grid(row = 0, column = 0)
myLable2.grid(row = 1, column = 0)

root.mainloop()