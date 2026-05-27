text = input("Enter a string: ")

special = "/*@&!$^"
words = ""

for ch in text:
    if ch in special:
        words = words + "#"
    else:
        words = words + ch

print(words)