def sum_odd_even( ):
  odd = 0 
  even= 0
  for i in range(1,1000):
      if i%2==0:
       even+=i
      else:
        odd+=i
  print(even)
  print(odd)
  print(abs(even-odd))

sum_odd_even()


