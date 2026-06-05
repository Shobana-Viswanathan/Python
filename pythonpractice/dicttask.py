def words(n):

    ans = {
        '0':'ZERO',
        '1':'ONE',
        '2':'TWO',
        '3':'THREE',
        '4':'FOUR',
        '5':'FIVE',
        '6':'SIX',
        '7':'SEVEN',
        '8':'EIGHT',
        '9':'NINE'
    }

    for i in str(n):
        print(ans[i], end=" ")

n1 = int(input("Enter number: "))
words(n1)