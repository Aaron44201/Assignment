#Aaron Bentley
#23/09/14
#Assignment statement spot check 2

weight = int(input("please enter weight in whole grams: "))

onehundred = (weight // 100)
remainder = (weight % 100)
fifty = (remainder // 50)
remainder2 = (remainder % 50)
ten = (remainder2 // 10)
remainder3 = (remainder2 % 10)
five = (remainder3 // 5)
remainder4 = (remainder3 % 5)
two = (remainder4 // 2)
remainder5 = (remainder4 % 2)
one = (remainder5 // 1)

print("""The masses you require are:
{0} 100g
{1} 50g
{2} 10g
{3} 5g
{4} 2g
{5} 1g""".format (onehundred,fifty,ten,five,two,one))

