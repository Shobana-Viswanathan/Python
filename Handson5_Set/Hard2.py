from itertools import combinations
s = list(map(int,input("Enter set values : ").split()))
target = int(input("Enter target sum : "))
result = []
for i in range(1,len(s)+1):
    for j in combinations(s, i):
        if sum(j)==target:
            result.append(set(j))
print(result)