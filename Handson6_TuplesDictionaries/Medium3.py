k = int(input("Enter k: "))
n = int(input("Enter number of tuples: "))

test_list = []

for i in range(n):
    test_list.append(tuple(map(int, input().split())))

res = []

for i in test_list:
    if len(i) != k:
        res.append(i)

print(res)