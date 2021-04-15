
f = open("rosalind_rna.txt", "rt")
trans = []
lines = f.readline()
stripped = list(lines.strip())

for x in stripped:
    if x == "T":
        trans.append("U")
    else:
        trans.append(x)

trans = "".join(trans)

print(trans)



