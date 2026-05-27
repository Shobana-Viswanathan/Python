t=(10,20,30,40,50)
print(id(t))
t=(100,) + t [1:]
print(t)
print(id(t))