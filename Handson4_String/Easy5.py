str1 = input("Enter a string:")

lowercase = ""
uppercase = ""

for ch in str1:
    if ch.islower():
        lowercase += ch
    else:
        uppercase += ch

result = lowercase + uppercase
print(result)
