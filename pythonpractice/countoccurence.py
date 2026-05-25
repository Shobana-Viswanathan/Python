str=input("Enter string: ")
tot_dig=0
tot_letter=0
for s in str :
    if s.isnumeric():
        tot_dig += 1
    elif s.isalpha():
        tot_letter += 1
    else:
        pass
print("Total digits: ",tot_dig)
print("Total letters: ",tot_letter)