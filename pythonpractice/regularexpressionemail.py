import re 
email=r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
text="Contact us at trainer@smartcliff.in or gayathri.manoj@smaertcliff.in"
found=re.findall(email,text)
if found:
    print("Email found",found)
else:
    print("Not found")