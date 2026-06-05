import re
text="Alan Turing was a pioneer of theoretical computer science and artificial intelligence.He was born on 23 June 1912 in Maida Vale,London"
res=re.search('computer',text)
print("Match Object {}".format(res))
print("-"*30)
print("group method output=",res.group())
print("-"*30)
print("Start method output=",res.start())
print("-"*30)
print("end method output=",res.end())
print("-"*30)
print("span method output=",res.span())
print("-"*30)
print("re attribute output=",res.re)
print("-"*30)
print("string attribute output=",res.string)
print("-"*30)
#example of usinng r as prefix
text=r'search \\n in this string'
res=re.search(r"\\",text)
print("With r prefix =",res)