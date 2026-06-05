try:
    dict={}
    n=int(input("Enter number of elements: "))
    for i in range(n):
        key=input("Enter key: ")
        value=input("Enter value: ")
        dict[key]=value
    print(dict["name"])
except KeyError:
    print("Error: Key not found!")