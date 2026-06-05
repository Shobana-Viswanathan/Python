str1 = input("Enter string: ")

words = str1.split()

for i in words:
    if i.isalnum() and not i.isalpha():
        print(i)