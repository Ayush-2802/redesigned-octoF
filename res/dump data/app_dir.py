import os

dir_1 = ("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\")
dir_2 = ("C:\\Program Files (x86)\\")
dir_3 = ("C:\\Program Files\\")

a = os.listdir(dir_1)
b = os.listdir(dir_2)
c = os.listdir(dir_3)

d = a[1]
print(d)
print(a)
print(b)
print(c)

import os
path = dir_1
if os.path.isdir(path):
    print("\nIt is a directory folder")
elif os.path.isfile(path):
    print("\nIt is a normal app file")
else:
    print("It is a special file (socket, FIFO, device file)" )
print()
