total = int(input())
rabbit = int(input())
deer = int(input())
birds = int(input())
squirrels = int(input())

rem = total - (rabbit + deer + birds + squirrels)

if rem == 1:
    print("Baby lion is well behaved")

elif rem > 1:
    print("Baby lion is mischievous")

else:
    print("Counted wrongly")