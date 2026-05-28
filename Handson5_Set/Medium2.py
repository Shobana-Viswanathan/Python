def set_comprehension(n):
   ele={x ** 2 for x in range(1,n+1)  }
   print(ele)
num = int(input())
set_comprehension(num)