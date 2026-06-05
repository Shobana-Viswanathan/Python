d = {}

n = int(input("Enter number of items: "))

for i in range(n):
    k = input("Key: ")
    v = int(input("Value: "))
    d[k] = v

search = input("Search key: ")

try:
    print(d[search])
except:
    print("Key Not found")