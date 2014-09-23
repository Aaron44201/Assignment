#Aaron Bentley
#23/09/14
#Assignment statement spot check

width = int(input("please enter pool width: "))
length = int(input("please enter pool length: "))
depth = int(input("please enter pool dept: "))
main_section_volume = length * width * depth
circle_radius = width/2
circle_area = 3.14 * (circle_radius*circle_radius)
half_circle_volume = (circle_area/2) * depth
pool_volume = main_section_volume + half_circle_volume
print("The pools volume is {0}".format (pool_volume))
