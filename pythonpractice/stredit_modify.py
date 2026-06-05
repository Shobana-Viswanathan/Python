greet="Hello,world!"
#greet[0]='J'
new_greet='J' + greet[1::]
print(new_greet)
new_greet='J' + greet[6::]
print(new_greet)
new_greet='J' + greet[-6:-1:]
print(new_greet)