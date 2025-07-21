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
        print(categories[el], temp[el].get(), values[el].get())
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
    return categories

def get_statistics(frame):
    canvas = Canvas(bg="white", width=250, height=200)
    canvas.grid()
    for i in range(len(get_chosen_categories())):
        wb = load_workbook("document.xlsx")
        ws = wb.active
        wasted = ws.cell(row=i+3, column=3).value
        left = ws.cell(row=i+3, column=2).value
        left_percent = left/(wasted + left)
        print(left_percent)
        Label(frame, text="Осталось").grid(row=i+1, column=0)
        Label(frame, text=str(left)).grid(row=i+1, column=1)
        Label(frame, text="Потрачено").grid(row=i+1, column=2)
        Label(frame, text=str(wasted)).grid(row=i+1, column=3)
        canvas.create_rectangle(25, 20+30*i, 25+200*left_percent, 40+30*i, fill="blue")
        # rect_center_x = 
        canvas.create_text(50, 100, text=("Осталось: "+str(left)))
        canvas.create_rectangle(25+200*left_percent, 20+30*i, 225, 40+30*i, fill="red")