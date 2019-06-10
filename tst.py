import os
import xlrd


def load_from_file(file):
    group_list = []
    workbook = xlrd.open_workbook(os.path.join(os.path.dirname(os.path.abspath(__file__)), "%s.xlsx" % file))
    worksheet = workbook.sheet_by_index(0)
    for i in range(10):
        group_list.append(worksheet.cell(i, 0).value)
    print(group_list)
    return group_list

load_from_file("groups")
