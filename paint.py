height = input("How high are the walls?: \n")
length = input("What is the length of the room? \n")
depth = input("What is the depth of the room? \n")

surface_area = 2*length*height + 2*depth*height - (length*depth)
ceiling = depth * length
print "The walls will need",surface_area,"sq ft of paint.  If you are going to paint the celing, you'll need",ceiling,"sq ft of additional paint."