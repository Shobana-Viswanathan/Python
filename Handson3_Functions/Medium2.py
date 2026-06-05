def prime (n,m):
    if(n<m):
     for i in range (n,m+1):
        for j in range (2,i):
            if i % j == 0 :
                break
        else :
         print(i)
    else :
       print("Provide valid input")
    
    
num1=int(input())
num2=int(input())
prime(num1,num2)
