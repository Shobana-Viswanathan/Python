def increment(list2):
    for i in range(0,len(list2)):
        list2[i] += 5
    print("Refrence of list inside the function:",id(list2))
list1=[10,20,30,40,50,60,70]
print("Reference of list in main:",id(list1))
print("The list before the function call:")
print(list1)
increment(list1)
print("The list after function call:")
print(list1)