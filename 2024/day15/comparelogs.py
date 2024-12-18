from mymodule import *

a = get_lines('answer.log')
b = get_lines('mylog.log')

for i in range(len(a)):
    if a[i] != b[i]:
        print(f"step {i} {a[i]} {b[i]}")
        exit(0)
        
print('match')