n = int(input(" "))
i = 0
for i in range(1, i<=n, 2):
    if i%2==0:
      odd+=i
    else:
       even+=i-1
print(even)
print(odd)