from datetime import date, timedelta
from openpyxl import load_workbook
from tkinter import *

def get_zero(num):
    if num < 10:
        result = '0' + str(num)
    else:
        result = str(num)
    return result

def get_week():
    today = date.today()
    first_day = today - timedelta(today.weekday())
    last_day = first_day + timedelta(7)
    return get_zero(first_day.day)+ "." + get_zero(first_day.month) + " - " + get_zero(last_day.day) + "." + get_zero(last_day.month)

def enter_categories(temp, categories, values, frame):
    wb = load_workbook("categories.xlsx")
    ws = wb.active
    i = 1
    for el in range (len(temp)):
        # print(categories[el], temp[el].get(), values[el].get())
        if temp[el].get() == 1:
            ws.cell(1, i, value=categories[el])
            val = values[el].get()
            try:
                val = int(val)
                ws.cell(2, i, value=val)
            except:
                Label(frame, text="Значения не должны содержать буквы").grid()
                return 1
            i += 1
    frame.destroy()
    print("works")
    wb.save("categories.xlsx")

def get_all_categories():
    return open("list of categories.txt", "r", encoding="utf-8").read().split(", ")

def get_chosen_categories():
    categories = []
    values = []
    wb = load_workbook("categories.xlsx")
    ws = wb.active
    i = 1
    while True:
        val = ws.cell(row=1, column=i).value
        i += 1
        if val == None:
            break
        else:
            categories.append(val)
            values.append(ws.cell(row=2, column=i-1).value)
    return [categories, values]

def get_statistics():
    canvas = Canvas(bg="white", width=350, height=300)
    canvas.grid()
    canvas.create_oval(25, 10, 45, 30, fill="blue")
    canvas.create_text(50, 40, text=("Осталось"))
    canvas.create_oval(205, 10, 225, 30, fill="red")
    canvas.create_text(200, 40, text=("Потрачено"))
    for i in range(len(get_chosen_categories()[0])):
        wb = load_workbook("document.xlsx")
        ws = wb.active
        canvas.create_text(50,70+30*i, text=(ws.cell(row=i+3, column=1).value))
        wasted = ws.cell(row=i+3, column=3).value
        left = ws.cell(row=i+3, column=2).value
        left_percent = left/(wasted + left)
        canvas.create_rectangle(100, 60+30*i, 100+200*left_percent, 80+30*i, fill="blue")
        if left_percent > 0.1:
            canvas.create_text(100+100*left_percent, 70+30*i, text=(str(left)))
        # rect_center_x = 
        canvas.create_rectangle(100+200*left_percent, 60+30*i, 325, 80+30*i, fill="red")
        if left_percent < 0.9:
           canvas.create_text(225+100*left_percent, 70+30*i, text=(str(wasted)))

def add_new_expence(root):
    frame = Frame(root,background='pink', width=400, height=400)
    frame.grid(row=0, column=0, rowspan=2)
    frame.grid_propagate(0)
    [all_categories, all_values] = get_chosen_categories()
    print(all_values)
    for i in range(len(all_categories)):
        label = Label(frame, text=all_categories[i])
        label.grid(row=i, column=0)
        entry = Entry(frame, )
        entry.insert(index=0, string=all_values[i])
        entry.grid(row=i, column=1)
    btn = Button(frame, text="Подтвердить")
    btn.grid(columnspan=2)