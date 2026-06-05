held = int(input("Enter number of classes held: "))
attended = int(input("Enter number of classes attended: "))
percentage = (attended / held) * 100
if percentage >= 75:
    print(f"{int(percentage)}% Allowed")
else:
    medical = input("Do you have a medical cause? (Y/N): ")
    if medical == 'Y':
        print(f"{int(percentage)}% Allowed")
    else:
        print(f"{int(percentage)}% Not allowed")