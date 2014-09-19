#Aaron Bentley
#19/09/14
#money counting

amount = int(input("Please input your amount of money: "))

twenty = amount // 20
remainder = amount % 20
ten = remainder // 10
remainder2 = remainder % 10
five = remainder2 // 5
remainder3 = remainder2 % 5
two = remainder3 // 2
remainder4 = remainder3 % 2
one = remainder4 // 1

print("The answer is: ")
print("{0} twenty pound notes".format (twenty))
print("{0} ten pound notes".format (ten))
print("{0} five pound notes".format (five))
print("{0} two pound coins".format (two))
print("{0} one pound coins".format (one))
      
