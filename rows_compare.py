import os, glob, openpyxl, string

path_a = "C:\\Users\\pisharamsomarajanh\\Desktop\\Excel_Exports\\CPF_10msec"
os.chdir(path_a)
a = glob.glob('*.xlsx')
path_b = "C:\\Users\\pisharamsomarajanh\\Desktop\\Excel_Exports\\Main\\CP_Flap\\CPF_10ms"
os.chdir(path_b)
b = glob.glob('*.xlsx')

count_a = dict()
count_b = dict()

for fn_a in a:
    wb = openpyxl.load_workbook(path_a + "\\" + fn_a)
    sheet = wb.worksheets[0]
    row_count = sheet.max_row
    count_a[fn_a.replace('.xlsx', '')] = row_count

for fn_b in b:
    wb = openpyxl.load_workbook(path_b + "\\" + fn_b)
    sheet = wb.worksheets[0]
    row_count = sheet.max_row
    count_b[fn_b.replace('.xlsx', '')] = row_count

for key, val in count_a.items():
    if count_a[key] != count_b[key]:
        print(key)
        
    
        
