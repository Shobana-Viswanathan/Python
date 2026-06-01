d = {}

d[0] = input("Value for key 0: ")
d[2] = input("Value for key 2: ")
d[3] = int(input("Value for key 3: "))
d[2] = input("Updated value for key 2: ")

v1 = input("Nested value 1: ")
v2 = input("Nested value 2: ")

d[5] = {'Nested': {'1': v1, '2': v2}}

print(d)