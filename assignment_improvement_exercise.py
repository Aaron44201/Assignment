#john bain
#variable improvement exercise
#05-09-12

import math

radius = float(input("please enter the radius of the circle: "))

circumfrence = 2* math.pi * radius
circumfrence = round(circumfrence,2)

area = math.pi * radius **2
area = round(area,2)

print("The circumference of this circle is {0}.".format(circumfrence))
print("The area of this circle is {0}.".format(area))
