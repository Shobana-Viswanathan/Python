name=input()
item=int(input())
if item < 10 :
    print(name,item*12)
elif item <= 10 and item < 99 :
    print(name,item*10)
elif item > 100 :
    print(name,item*7)