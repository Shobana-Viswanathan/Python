def sum_odd_even(n):
  odd = 0 
  even= 0
  for i in range(1,n+1):
      if i%2==0:
       even+=i
      else:
        odd+=i
  print(even)
  print(odd)

num=int(input())
sum_odd_even(num)
