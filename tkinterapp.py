from tkinter import *
from tkinter import ttk
from funcs import *

root = Tk()
root.title("Планирование финансов")
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))

Label(text="Hello METANIT.COM").pack()
categories = get_categories()
temp = []
for el in categories:
    temp.append(IntVar())
    ttk.Checkbutton(text=el, variable=temp[len(temp)-1]).pack()
    # ttk.Label(textvariable=temp[len(temp)-1]).pack()
root.mainloop()