def pascal_triangle(num):
    # initialize the first value of the pascal triangle
    pascal = [1]
    # prints the initial value
    print(pascal)
    # the first loop resets the temporary list
    for i in range(0, num):
        # temporary list is used to hold the currently being added values
        tempPascal = []
        #adds the initial value of 1 for the temporary list
        tempPascal.append(1)
        #this loop is used to go through the pascal list that holds the previous values, -1 at the end to avoid out of index
        for j in range(0, len(pascal)-1):
            # adds the values depending on the index and appending it to the temporary list
            tempPascal.append(pascal[j]+pascal[j+1])
        # makes sure there is 1 at the end of the temporary list
        tempPascal.append(1)
        # adds the values in the temporary list to the pascal list to be printed
        pascal = tempPascal
        print(pascal)

while True:
    while True:
        try:
            height = (int(input("Height of pascal's triangle (-1 to end): ")))
            break
        except ValueError:
            print("Please put an integer in!")
    if height == -1:
        print("program terminated!")
        break
    pascal_triangle(height)
