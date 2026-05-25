def area_circle(radius):
    print("Area of circle is: ",3.14*radius * radius)
def area_rectangle(length,breadth):
    print("Area of rectangle is: ",length * breadth)
def area_square(side):
    print("Area of sqaure is: ",side * side)

while True:
    print("Menu Driven Program")
    print("1. Area of circle")
    print("2. Area of rectangle")
    print("3.Area of square")
    print("4. Exit")
    choice=int(input("Enter the choice: "))
    if(choice==1):
       radius=int(input())
       area_circle(radius)
       
    elif (choice==2):
        length=int(input())
        breadth=int(input())
        area_rectangle(length,breadth)
      
    elif (choice==3):
        side=int(input())
        area_square(side)
        
    elif (choice==4):
        break
    else:
        print("Wrong choice")
    


        