input1 = input("Enter the String1:")
input2 = input("Enter the String2:")
n1 = len(input1)
for i in range(0,n1):
    print(input1[i]+input2[n1-i-1],end="")