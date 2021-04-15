f = open("rosalind_revc.txt", "rt")
line = list(f.readline().strip())
comp = []

for x in line:
    if x == "A":
        comp.append("T")
    elif x == "T":
        comp.append("A")
    elif x == "G":
        comp.append("C")
    elif x == "C":
        comp.append("G")
comp.reverse()
comp = "".join(comp)
print(comp)

f.close()

