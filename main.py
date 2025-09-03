from tkinter import *
from funcs import *
from openpyxl import *

wb = load_workbook("categories.xlsx")
ws = wb.active
if ws.cell(1,1).value==None:
    frame1.grid()
    Label(frame1, text="Выберите категории расходов: ").grid(row=0, column=0)
    categories = get_all_categories()
    temp = []
    entries = []
    row_num = 1
    for i in range(len(categories)):
        temp.append(IntVar())
        Checkbutton(frame1, text=categories[i], variable=temp[i]).grid(row=row_num, column=0)
        entry = Entry(frame1)
        entry.grid(row=row_num, column=1)
        entries.append(entry)
        row_num += 1
    btn = Button(frame1, text="Продолжить", command=lambda: enter_categories(temp, categories, entries, frame1))
    btn.grid(row=row_num, column=0)
    row_num += 1
else:
    get_statistics()
root.mainloop()