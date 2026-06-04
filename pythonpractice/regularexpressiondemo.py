import re
text="Alan Turing was a pioneer of theoretical computer science and artificial intelligence.He was born on 23 June 1912 in Maida Vale,London"
#search
res=re.search("^Alan.*London$",text)

print(type(res))
if(res):
    print("We have a match")
else:
    print("No match")
#findall
res1=re.findall("was",text)
print("Result= {} ".format(res1))
#span
res2=re.search("Turing",text)
print("Result={} and start,end position={}".format(res2,res2.span()))
#split
res3=re.split("a",text)
print("Result={}".format(res3))
print(type(res3))
print("-"*60)
#sub
res4=re.sub("theoretical","practical",text)
print("Result={}".format(res4))