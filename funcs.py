from datetime import date, timedelta
from openpyxl import load_workbook

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

def get_categories():
    return open("list of categories.txt", "r", encoding="utf-8").read().split(", ")

    # print("выберите категории из списка:")
    # for i in range(0, len(list)):
    #     print(str(i) + ". " + list[i])
    # return list(map(lambda x: int(x),input("введите номера категорий через запятую").split(",")))

#     wb = load_workbook("categories.xlsx")
#     ws = 
#     for el in chosen_categories:
