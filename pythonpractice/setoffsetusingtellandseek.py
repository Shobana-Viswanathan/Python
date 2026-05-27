print("Learning to move the file object")
fobject=open("test.txt","r+")
print(fobject.tell())
fobject.seek(0)
print("Now going to use seek")
fobject.seek(5)
print("Current position after seek:", fobject.tell())
print("Text from position 5:")
print(fobject.read())




