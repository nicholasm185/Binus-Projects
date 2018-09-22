# user input for the height of the first half
while True:
    try:
        height = int(input("Input any number: "))
        break
    except ValueError:
        print("Please input integers")

# tell user the height of diamond
print("Your diamond will have the height of: "+str(height*2-1))

# variables
# height1 used for second half counter
height1 = height
stars = 1

# first half of diamond
while height > 1:
    print(" " * height + "*" * stars + "*" *(stars-1))
    stars += 1
    height -= 1

# second half of diamond
while height1 > 0:
    print(" " * height + "*" * stars + "*" * (stars-1))
    stars -= 1
    height += 1
    height1 -= 1
