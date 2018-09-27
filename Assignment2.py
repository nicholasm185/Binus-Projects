# function for question no.1
def kmp(name):
    name = name.replace("-","")
    shortened = ""
    i = 0
    while i < len(name):
        if name[i] == name[i].upper():
            shortened += name[i]
        i += 1
    print(shortened)

#function for question no.2
def modul42():
    list1 = []
    listMod = []
    for j in range (0,10):
        list1.append(int(input("Input an integer: ")))
    for i in range (0,10):
        listMod.append(list1[i] % 42)
    listMod = set(listMod)
    print("You have "+str(len(listMod))+" different results")

# function for question no.3
def aliceAndBob(numTry):
    winner = []
    while numTry > 0:
        number = int(input("Input a number: "))
        if number%2 == 0:
            winner.append("Bob")
        else:
            winner.append("Alice")
        numTry -= 1
    if winner.count("Bob") > winner.count("Alice"):
        print("Bob Wins!")
    else:
        print("Alice Wins!")

# function for question no.4
def cupsAndBall(moves):
    moveSet = []
    # a list to indicate the position which always starts at the very left
    position = [1,0,0]
    for i in range (0, moves):
        moveSet.append(str(input("Which moveset? (A,B,C): ")).upper)
    for j in range (0, len(moveSet)):
        # the ifs checks the input and switches the position according by their index
        if moveSet[j] == "A":
            position[0],position[1] = position[1],position[0]
        if moveSet[j] == "B":
            position[2],position[1] = position[1],position[2]
        if moveSet[j] == "C":
            position[0],position[2] = position[2],position[0]
    # prints the position of the ball, +1 due to how indexing works
    print("The ball is in the position " + str(position.index(1)+1))



# user calls for which function
status = input("""
******************************************
* Which fucntion would you like to call? *
* Function 1: \"Name Shortener\"           *
* Function 2: \"modul42\"                  *
* Function 3: \"aliceAndBob\"              *
* Function 4: \"cupsAndBall\"              *
* Type \"exit\" to end program             *
******************************************
Input: """)
# if statement checks user input
if status == "1":
    kmp(input("Insert a name (capitalized): "))
elif status == "2":
    modul42()
elif status == "3":
    aliceAndBob(int(input("Insert the number of tries: ")))
elif status == "4":
    cupsAndBall(int(input("How many moves?")))
elif status.lower() == "exit":
    print("Program terminated")
else:
    print("Unknown command!")
