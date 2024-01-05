m, n = map(int, input().split())

ball = list(range(1, m+1))

for _ in range(n):
    i, j = map(int, input().split())
    ball[i-1], ball[j-1] = ball[j-1], ball[i-1]

print(" ".join(map(str, ball)))
