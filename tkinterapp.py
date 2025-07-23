from tkinter import *
from tkinter import ttk
from funcs import *
from openpyxl import *

# def addEntry(row_num):
#     entries[row_num - 1] = ttk.Entry()
#     entries[row_num - 1].grid(frame1, row=row_num, column=1)

root = Tk()
root.title("Планирование финансов")
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
wb = load_workbook("categories.xlsx")
ws = wb.active
if ws.cell(1,1).value==None:
    frame1 = Frame(root, background='pink')
    frame1.grid()
    Label(frame1, text="Выберите категории расходов: ").grid(row=0, column=0)
    categories = get_all_categories()
    temp = []
    entries = []
    row_num = 1
    for i in range(len(categories)):
        temp.append(IntVar())
        ttk.Checkbutton(frame1, text=categories[i], variable=temp[i]).grid(row=row_num, column=0)
        entry = ttk.Entry(frame1)
        entry.grid(row=row_num, column=1)
        entries.append(entry)
        row_num += 1
    btn = ttk.Button(frame1, text="Продолжить", command=lambda: enter_categories(temp, categories, entries, frame1))
    btn.grid(row=row_num, column=0)
    row_num += 1
else:
    canvas = get_statistics()
    # frame1 = Frame(root, background='pink')
    # frame1.grid()
    # Label(frame1, text="Rfeirihuvuo").grid(row=0, column=0)
    # btn = ttk.Button(canvas, text="Добавить новый расход")
    # btn.grid()
root.mainloop()