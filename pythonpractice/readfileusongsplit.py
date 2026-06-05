myobject=open("myfile.txt","r")

var=myobject.readlines()
for line in var:
    #spilit single word
    #words=line.split()
    #splitlines
    words=line.splitlines()
    print(words)
