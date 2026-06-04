import re
pattern=r'\b\w+ing\b'
text="Walking and talking are important activities."

res=re.search(pattern,text)
if res :
    print("Match found:",res.group())
else:
    print("Not found")

#res=re.findall(pattern,text)
#print("Match found:",res) o/p:Match found: ['Walking', 'talking']