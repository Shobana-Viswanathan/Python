from collections import Counter

n = int(input("Enter number of tuples: "))

lst = []

for i in range(n):
    a, b = map(int, input().split())
    lst.append((a, b))

c = Counter(lst)

ans = 0

for i in c:
    if i[0] < i[1]:
        ans += min(c[i], c[(i[1], i[0])])

print(ans)