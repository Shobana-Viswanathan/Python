total=0
while True :
   price=int(input("Enter the price of the item: "))
   quantity=int(input("Enter the quantity of the item: w"))
   option=input("Do you want to enter another item?(yes/no)")
   total=total+(price*quantity)
   if(option=='no'):
    break
print("Total Price: ",total)