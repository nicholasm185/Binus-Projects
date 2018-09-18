height = int(input("Input any number: "))
height1 = height + 1
stars = 1
stars1 = 1
while height > 0:
    print(" " * height + "*" * stars + "*" *(stars-1))
    stars += 1
    height -= 1

while height1 > 0:
    print(" " * (height) + "*" * stars + "*" * (stars-1))
    stars -= 1
    height += 1
    height1 -= 1
