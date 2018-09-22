height = int(input("Input any number: "))
stars = 1

while height > 0:
    print(" " * height + "*" * stars + "*" *(stars-1))
    stars += 1
    height -= 1
