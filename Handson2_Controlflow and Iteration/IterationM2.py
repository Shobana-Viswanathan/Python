n = input()

if len(n) == 5:

    rev = ""

    for i in n:
        rev = i + rev

    print(rev)

else:
    print("Not a valid number")