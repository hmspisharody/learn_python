import os, glob

path_a = "C:\\Users\\pisharamsomarajanh\\Desktop\\Excel_Exports\\MP_10msec"
os.chdir(path_a)
a = glob.glob('*.xlsx')
path_b = "C:\\Users\\pisharamsomarajanh\\Desktop\\Excel_Exports\\Main\\MP\\MP_10ms"
os.chdir(path_b)
b = glob.glob('*.xlsx')

a_only = []
b_only = []

print("Only in '" + path_a + "'\n" + "=============================") 
for fna in a:
    a_flag = 1
    for fnb in b:
        if fna == fnb:
            a_flag = 0
            break
    if a_flag == 1:
        a_only.append(fna)
        print(fna)
        
print("\nOnly in '" + path_b + "'\n" + "=============================")
for fnb in b:
    b_flag = 1
    for fna in a:
        if fna == fnb:
            b_flag = 0
            break
    if b_flag == 1:
        b_only.append(fnb)
        print(fnb)
        
            
        
