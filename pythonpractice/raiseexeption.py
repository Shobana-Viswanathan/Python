try:
    num=int(input())
    if(num<=0):
        raise ValueError ("Negative number")
except ValueError as e:
    print(e)
print("I am successfully handled")    
