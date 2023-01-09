import openpyxl
import os


folder_path = r'D:\mitesh\python\nnc'
excel_filename = 'NNC_Photography_Contes_2023_Participants.xlsx'

wb = openpyxl.load_workbook(os.path.join(folder_path, excel_filename))

for i, row in enumerate(wb.active.rows):
    if i == 0:
        continue

    if row[0].value == None:
        break

    user_folder_name = row[2].value
    new_user_folder_name = str(int(row[1].value))

    print(i, user_folder_name)


    user_folder_path = os.path.join(folder_path, user_folder_name)
    new_user_folder_path = os.path.join(folder_path, new_user_folder_name)

    # Rename folder
    os.rename(user_folder_path, new_user_folder_path)

    files = os.listdir(new_user_folder_path)
    for f, file in enumerate(files, 1):
        file_path = os.path.join(new_user_folder_path, file)
        new_file_path = os.path.join(new_user_folder_path, str(f) + os.path.splitext(file)[1])

        # Rename file
        os.rename(file_path, new_file_path)

wb.close()
