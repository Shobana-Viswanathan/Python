total = 0

while True:

    price = int(input("Enter the price of the item: "))
    quantity = int(input("Enter the quantity of the item: "))

    total = total + (price * quantity)

    choice = input("Do you want to enter another item?(yes/no) ")

    if choice.lower() == "no":
        break

print("Total Cost:", total)
