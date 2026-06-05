k = int(input("Enter k: "))
n = int(input("Enter number of tuples: "))

lst = []

for i in range(n):
    a, b = map(int, input().split())
    lst.append((a, b))

d = {}
res = []

for i in lst:
    if d.get(i[0], 0) < k:
        res.append(i)
        d[i[0]] = d.get(i[0], 0) + 1

print(res)