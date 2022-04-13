def repetidos (a):
    l = []
    for i in a:
        if i not in l:
            l.append(i)
    l.sort()
    return l

a = [1, 1, 2, 1, 3, 4, 3, 6, 7, 6, 7, 8, 6, 10, 9, 13, 14, 3, 17, 21, 13, 5]

a = repetidos(a)
print (a)
import os
os.system("pause")