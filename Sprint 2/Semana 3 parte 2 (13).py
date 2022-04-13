a=[] 
speed = {'jan':47, 'feb':52, 'march':47, 'April':44, 'May':52, 'June':53, 'july':54, 'Aug':44,
'Sept':54}

for b, c in speed.items():
    a.append(c) 
a = list(set(a)) 
print(a)
import os
os.system("pause")