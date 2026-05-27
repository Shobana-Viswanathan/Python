fobject=open("test2.txt",'w')
print("Adding the contents to write in file")

fobject.write("Hey I have started using files in python\n")
print("Now reading the content from the file")
fobject=open("test2.txt",'r')
for str in fobject:
    fobject.readlines()
    print(str)
