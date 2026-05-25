def findMax(* numbers):
    max=0
    for i in numbers:
        if(max < i): max=i
    return max

print("Maximum:",findMax(10,20,30,40,50))