# user input for the height of the first half
height = int(input("Input any number: "))

# variables
# height1 used for second half
height1 = height + 1
stars = 1
# stars1 used for second half
stars1 = 1

# first half of diamond
while height > 0:
    print(" " * height + "*" * stars + "*" *(stars-1))
    stars += 1
    height -= 1

# second half of diamond
while height1 > 0:
    print(" " * (height) + "*" * stars + "*" * (stars-1))
    stars -= 1
    height += 1
    height1 -= 1
