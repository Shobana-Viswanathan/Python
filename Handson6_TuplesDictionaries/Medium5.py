words = input("Enter words: ").split()
chars = set(input("Enter characters: ").split())

for i in words:
    if set(i) <= chars:
        print(i, end=" ")