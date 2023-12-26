a = int(input())
b = list(map(int,input().split()))
c = int(input())
d = 0
for i in b:
    if c == i:
        d += 1    
print(d)
