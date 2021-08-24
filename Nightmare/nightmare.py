import os

imports = ""
prints = [""]

file = open("Nightmare/out", 'r')
txt = file.read()
file.close()

file = open("Nightmare/Nightmare/__init__.py", 'w')
file.write("")
file.close()

for i in range(len(txt) // 100):
    prints.append("")

for n in range(len(txt)):
    file = open("Nightmare/Nightmare/f" + str(n) + ".py", 'w')
    file.write('v' + str(n) + " = \'\'\'" + txt[n] + "\'\'\'")
    file.close()
    imports += "import Nightmare.f" + str(n) + "\n"
    prints[n // 100] += '+ Nightmare.f' + str(n) + '.v' + str(n) + ' '


for j in range(len(prints)):
    prints[j] = prints[j][2:]

file = open("Nightmare/main.py", 'w')
file.write(imports)
file.close

file = open("Nightmare/main.py", 'a')

for k in range(len(prints)):
    file.write("\np" + str(k) + " = " + prints[k])

file.write("\nprint (p0")

for l in range(len(prints) - 1):
    file.write(" + p" + str(l + 1))

file.write(')')
#file.close()