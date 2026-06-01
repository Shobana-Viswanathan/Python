string1 = input("Enter the string: ")

print("Initial String with use of Triple Quotes:")
print(string1)

print("Escaping Single Quote:")
print(string1.replace("'", "\\'"))

print("Escaping Double Quotes:")
print(string1.replace('"', '\\"'))

print("Escaping Backslash:")
print(string1.replace("\\", "\\\\"))