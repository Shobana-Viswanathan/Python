total = 0
count = 1

while True:

    price = float(input(f"Enter the price of the {count} item: "))
    quantity = int(input(f"Enter the quantity of the {count} item: "))

    total = total + (price * quantity)

    choice = input("Do you want to enter another item? (yes/no): ")

    if choice.lower() == "no":
        break

    count += 1

<<<<<<< HEAD
print("Total Price:", int(total))
=======
print("Total Price:", int(total))
>>>>>>> da7e9444e6ce8e8d4a0ad2241b51c1bd32d65326
