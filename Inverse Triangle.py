num = 10
stars = 0
blanks = 10
while num >= 0:
    print(" "*blanks+"*"*stars)
    blanks -= 1
    stars += 1
    num -= 1

print("You're welcome!")
