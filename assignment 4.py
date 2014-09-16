#Aaron Bentley
#16/09/2014
#Exercise 4 development exercises

print("Enter all values in metres")
length = int(input("Pool lenght: "))
width = int(input("Pool width: "))
depth_shallow = int(input("Pools shallow depth: "))
depth_deepest = int(input("Pools deepest depth: "))
depth_diff = (depth_deepest - depth_shallow)
subracted_amount = (depth_diff)*(length)*(width)
volume = (length*width*depth_deepest)
answer = (volume-subracted_amount)
print("The volume is: {0}metres cubed".format (answer))
