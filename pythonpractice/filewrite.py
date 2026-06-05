myobject=open("myfile.txt",'w')
#write method
myobject.write("Hey I have started using files in python\n")
marks=50
myobject.write(str(marks))
#writelines method
lines=["Hello Everyone\n","Writing multiline strings\n","This is the #third line"]
myobject.writelines(lines)
myobject.close()

