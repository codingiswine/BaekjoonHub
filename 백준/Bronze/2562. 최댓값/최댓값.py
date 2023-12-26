a = [ ]
for i in range(9):
    n = int(input())
    a.append(n)

a_max = max(a)
b_inx = a.index(a_max) + 1

print(a_max)
print(b_inx)
