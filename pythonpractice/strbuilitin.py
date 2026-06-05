str="Good Day"
#upper
res=str.upper()
print(res)
#lower
print(str.lower())
#find
word='apaple'
print(word.find('p'))
print(word.find('ap',2))
#replace
msg="Good mrng"
print(msg.replace("Good","Happy"))
#count
print(msg.count('o'))
#captialize
#captialize the first character changed to caps remaining all in lower case
demo="python learing"
print(demo.capitalize())
word2="ss11"
#isalnum
print(word2.isalnum())
word3="hii"
#isalpha
print(word3.isalpha())
#endswith
text="Python is easy to learn"
print(text.endswith("to learn"))
#startwith
print(text.startswith("to learn"))