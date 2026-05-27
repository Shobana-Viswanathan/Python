list1=[10,20,30,40,50,60,70]
while True:
 print("Menu Driver")
 print("1.Append an element")
 print("2.Insert an element")
 print("3.Appenda list to the given list")
 print("4.Modifyan existing element")
 print("5.Delete an existing element from its position")
 print("6.Delete an existing element with a given value")
 print("7.Sort the list in ascending order")
 print("8.Sort the list in descending order")
 print("9.Display the list")
 print("10.Exit")
 choice=int(input())
 if choice == 1 :
   elem=int(input())
   list1.append(elem)
 elif choice == 2 :
  index=int(input("Enter the index:"))
  element=int(input("Enter the element to insert"))
  list1.insert(index,element)
 elif choice == 3:
  index=int(input("Enter the index:"))
  element=int(input("Enter the element to insert"))
  list1.extend(index,element)
 elif choice == 4 :
  index=int(input("Enter the index:"))
  element=int(input("Enter the element:"))
  list1[index] = element
  
 elif choice == 5 :
  element=int(input("Enter the element:"))
  list1.remove(element)
 elif choice == 6 :
  index=int(input("Enter the index:"))
  list1.pop(index)
 elif choice == 7 :
  list1.sort()
 elif choice == 8 :
  list1.sort(reverse=True)
 elif choice == 9:
  print(list1)
 elif choice == 10 :
  break
 
 

