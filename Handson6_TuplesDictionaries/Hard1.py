n = int(input("Enter number of tuples: "))

lst = []

for i in range(n):
    word = input("Enter word: ")
    num = int(input("Enter number: "))
    lst.append((word, num))

lst.sort(key=lambda x: x[1])

print(lst)