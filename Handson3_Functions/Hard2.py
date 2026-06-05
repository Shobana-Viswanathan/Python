def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return abs(n1 - n2)

def multiply(n1, n2):
    return n1 * n2

def calculator(operation, operand1, operand2):
    return operation(operand1, operand2)


n1 = int(input("n1: "))
n2 = int(input("n2: "))

m1 = int(input("m1: "))
m2 = int(input("m2: "))

s1 = int(input("s1: "))
s2 = int(input("s2: "))

print("Add:", calculator(add, n1, n2))
print("Subtract:", calculator(sub, m1, m2))
print("Multiply:", calculator(multiply, s1, s2))