import openpyxl
import os


folder_path = r'D:\mitesh\python\nnc'
excel_filename = 'NNC_Photography_Contes_2023_Participants.xlsx'

wb = openpyxl.load_workbook(os.path.join(folder_path, excel_filename))

for i, row in enumerate(wb.active.rows):
    if i == 0:
        continue

    print(i, row)
    
    user_folder_name = row[2].value
    os.mkdir(os.path.join(folder_path, user_folder_name))

wb.close()
