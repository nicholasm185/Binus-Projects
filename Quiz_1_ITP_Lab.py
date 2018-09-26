top = {}
mid = {}
bot = {}
space = 15

while True:
    status = str(input("Would you like to use the refrigerator? Y/N "))
    if status.upper() == "Y":
        while True:
            try:
                addOrTake = str(input("Would you like to add take or clear or check? "))
                if addOrTake == "check":
                    break
                elif addOrTake == "clear":
                    shelf = str(input("Which shelf would you like to input? (top, mid, or bot) "))
                    break
                else:
                    shelf = str(input("Which shelf would you like to input? (top, mid, or bot) "))
                    item = str(input("What is the item? "))
                    change = int(input("How many? "))
                    break
            except ValueError:
                print("Invalid input, please try again!")

        if addOrTake == "take":
            change = 0 - change

        if addOrTake.lower() == "check":
            print("Top has:")
            print(top)
            print("Mid has: ")
            print(mid)
            print("Bot has: ")
            print(bot)
        else:
            if shelf == "top":
                if addOrTake == "clear":
                    print("You have taken ")
                    print(top)
                    top.clear()
                    print("Top is now empty!")
                else:
                    checkValue = top.get(item,0)+change
                    totalSpace = sum(top.values())+change

                    if totalSpace > space:
                        print("Not enough space! try again")
                    elif checkValue < 0:
                        print("You don't have that many "+item)
                    else:
                        top.update({item:checkValue})
                    print("Top has: ")
                    print(top)
            if shelf == "mid":
                if addOrTake == "clear":
                    print("You have taken ")
                    print(mid)
                    mid.clear()
                    print("Top is now empty!")
                else:
                    checkValue = mid.get(item,0)+change
                    totalSpace = sum(mid.values())+change

                    if totalSpace > space:
                        print("Not enough space! try again")
                    elif checkValue < 0:
                        print("You don't have that many "+item)
                    else:
                        mid.update({item:checkValue})
                    print("Mid has: ")
                    print(mid)
            if shelf == "bot":
                if addOrTake == "clear":
                    print("You have taken ")
                    print(bot)
                    bot.clear()
                    print("Top is now empty!")
                else:
                    checkValue = bot.get(item,0)+change
                    totalSpace = sum(bot.values())+change

                    if totalSpace > space:
                        print("Not enough space! try again")
                    elif checkValue < 0:
                        print("You don't have that many "+item)
                    else:
                        bot.update({item:checkValue})
                    print("Bot has: ")
                    print(bot)
    elif status.upper() == "N":
        print("Thanks for using the refrigerator!")
        break
