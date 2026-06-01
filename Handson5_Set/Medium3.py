n = int(input("Enter number of sets : "))
sets = []
for i in range(n):
    s = set(map(int, input().split()))
    sets.append(s)
common = sets[0]
for i in sets[1:]:
    common = common & i
print(len(common))