income=float(input("Enter your monthly income: "))
expenses=(input("Enter your expenses (space-separated)")).split()
sum= int(expenses[0]) + int(expenses[1]) + int(expenses[2])
print(sum)
remaining = income - sum
print("Remaining budget:$",remaining)

