d1 = {}
d2 = {}

n = int(input("Enter size: "))

for i in range(n):
    k = input("Key d1: ")
    v = int(input("Value d1: "))
    d1[k] = v

for i in range(n):
    k = input("Key d2: ")
    v = int(input("Value d2: "))
    d2[k] = v

v = list(d2.values())

res = {}

for i, j in enumerate(d1.keys()):
    res[j] = v[i]

print(res)