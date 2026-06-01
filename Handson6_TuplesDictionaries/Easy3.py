name = input("Enter string: ")
num = float(input("Enter number: "))

t1 = (1, name, num)

lst = list(map(int, input("Enter list elements: ").split()))
t2 = ("mouse", lst, (1, 2, 3))

print(t1)
print(t2)