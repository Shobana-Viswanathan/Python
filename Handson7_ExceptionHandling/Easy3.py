try:
    l=list(map(int,input("enter the list: ").split()))
    print(l[4])
except IndexError:
    print("Error: Index out of range!")