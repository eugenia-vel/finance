from openpyxl import Workbook, load_workbook
from funcs import get_week

current_week = get_week()
planned_money = [140, 1050, 700, 700, 450, 1050, 580, 3500]
try:
    wb = load_workbook('document.xlsx')
    ws = wb.active
except:
    wb = Workbook()
    ws = wb.active
    ws['A3'] = "Связь"
    ws['A4'] = "Электро"
    ws['A5'] = "Психиатр"
    ws['A6'] = "Одежда/обувь"
    ws['A7'] = "Копилка"
    ws['A8'] = "Гигиена"
    ws['A9'] = "На всякий случай"
    ws['A10'] = "Еда"
ws.freeze_panes = ws['B3']
i = 2
while ws.cell(1, i).value!=current_week:
    if ws.cell(1, i).value==None:
        ws.merge_cells(start_row=1, start_column=i, end_row=1, end_column=i+1)
        ws.cell(1, i).value = current_week
        ws.cell(2, i).value = "Осталось"
        ws.cell(2, i+1).value = "Потрачено"
        for j in range(3,11):
            ws.cell(j,i).value = planned_money[j-3]
            ws.cell(j,i+1).value = 0
    else:
        i += 2
command = ""
# q = quit, a = add
while command != "q":
    command = input("Введите a, чтобы добавить расход, или q, чтобы выйти: ")
    if command == "a":
        print("Выберите категорию:")
        for j in range(3, 11):
            print(str(j-2) + ". " + ws.cell(j, 1).value)
        categ = int(input("Введите номер категории: "))
        money = int(input("Введите сумму: "))
        ws.cell(categ+2, i).value = ws.cell(categ+2, i).value - money
        ws.cell(categ+2, i+1).value = ws.cell(categ+2, i+1).value + money
wb.save('document.xlsx')