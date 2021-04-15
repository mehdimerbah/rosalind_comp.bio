

f = open("rosalind_dna.txt", "rt")

listing = []
for line in f:

    listing = list(line)

a_c = 0
g_c = 0
c_c = 0
t_c = 0
for base in listing:
    if base == "A":
        a_c+=1
    elif base == "G":
        g_c+=1
    elif base == "C":
        c_c+=1
    elif base == "T": 
        t_c+=1


print(a_c, " ", c_c, " ", g_c, " ", t_c )

