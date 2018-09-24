# # question 1
def max_of_three(num1,num2,num3):
    numbers = [num1,num2,num3]
    numbers.sort()
    print(numbers[2])

max_of_three(input("num1"),input("num2"),input("num3"))

# # question 2
def listLen(list1):
    total = 0
    i=0
    for i in list1:
        total += 1
    print("The length of the string is: "+ str(total))


testList = [0, 1, 2, 3, 4]

print(testList)
listLen(testList)

# # question 3
def vowelCheck(string1):
    if string1.lower() == "a" or string1.lower() == "i" or string1.lower() == "u" or string1.lower() == "e" or string1.lower() == "o":
        print("It's a vowel!")
    else:
        print("It's not a vowel!")

vowelCheck(str(input("Insert a character: ")))

# # question 4
def reverse(string1):
    revString = string1[::-1]
    print(revString)

reverse(str(input("Insert a string: ")))

# # question 5
def is_member(a,x):
    for i in a:
        if i == x:
            print("Object found!")
            break
    else:
        print("Not Found!")


sampleList = [1,2,3,4]
is_member(sampleList,5)

# # question 6
def overlapping(list1,list2):
    i = 0
    j = 0
    status = False
    while i < len(list1):
        while j < len(list2):
            if list1[i] == list2[j]:
                print("True")
                status = True
                break
            j += 1
        i += 1
        j=0
    if status == False:
        print("False")


sampleList1 = [1,2,3,4]
sampleList2 = [4,5,6,7]
overlapping(sampleList1,sampleList2)

# # question 7
def generate_n_chars(mult,string):
    printable = ""
    for i in range(0,mult):
        printable += string
    print(printable)

generate_n_chars(5,"sample")

# question 8
def histogram(list):
    i = 0
    while i < len(list):
        print("*"*list[i])
        i += 1

testList = [2,4,1,5]
histogram(testList)

# # question 9
def listWord_lengths(list):
    i = 0
    inlist = []
    while i < len(list):
        inlist.append(len(list[i]))
        i += 1
    print(inlist)

testList = ["try", "my", "codes", "here"]
listWord_lengths(testList)

# question 10
def find_longest_word(list):
    i = 0
    longest = 0
    while i < len(list):
        if len(list[i]) > longest:
            longest = len(list[i])
        i += 1
    print(longest)

testList = ["try", "my", "codes are good", "here"]
find_longest_word(testList)

# # question 11
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def pangram(string):
    string = string.lower()
    string = string.replace(" ","")
    string = list(string)
    i = 0
    j = 0
    status = 0
    while i < len(string):
        while j < len(alphabet):
            if string[i] == alphabet[j]:
                status += 1
            j += 1
        if status <= 0:
                print("Not a pangram")
                break
        i += 1
        j=0
        status = 0
    else:
        print("pangram")

pangram("abcdefghijklmnopqrstuv wxyz")

# question 12
consonance = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]
vowel = ["a", "i", "u", "e", "o"]
def make_ing_form(verb):
    if verb[len(verb)-2:len(verb)+1] == "ie":
        verb = verb[:-2]
        verb = verb+"ying"
        print(verb)
    elif verb[-1] == "e":
        verb = verb[:-1]
        verb = verb+"ing"
        print(verb)
    elif (verb[-1] in consonance) and (verb[-2] in vowel) and (verb[-3] in consonance):
        verb = verb + verb[-1] + "ing"
        print(verb)
    else:
        verb = verb+"ing"
        print(verb)

make_ing_form(str(input("Insert an infinitive verb: ")))
