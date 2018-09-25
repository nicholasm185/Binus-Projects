alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
            "u", "v", "w", "x", "y", "z"]
capAlphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
               "V", "W", "X", "Y", "Z"]
encryptdic = {}
decipherdic = {}

rot = int(input("What is the rotation: "))

for l in range(0, len(alphabet)):
    rotator = l+rot
    if rotator >= len(alphabet):
        rotator = rotator - len(alphabet)
    encryptdic.update({alphabet[l]:alphabet[rotator]})
    encryptdic.update({capAlphabet[l]:capAlphabet[rotator]})
    decipherdic.update({alphabet[rotator]:alphabet[l]})
    decipherdic.update({capAlphabet[rotator]:capAlphabet[l]})

def encryptor(string):
    string = list(string)
    temp = ""
    for i in range(0, len(string)):
        if string[i] == " ":
            continue
        else:
            temp1 = encryptdic.get(string[i])
            string[i] = temp1
    print(temp.join(string))

def decryptor(string):
    string = list(string)
    temp = ""
    for i in range(0, len(string)):
        if string[i] == " ":
            continue
        else:
            temp1 = decipherdic.get(string[i])
            string[i] = temp1
    print(temp.join(string))

while True:
    ui = input("""
    ****************************************
    *Would you like to encrypt or decrypt? *
    *(1 for encrypt, 2 for decrypt         *
    * "exit" to end process
    ****************************************
    Input: """)
    if ui == "1":
        encryptor(input("Input your string: "))
    elif ui == "2":
        decryptor(input("Input your decrypted string: "))
    elif ui == "exit":
        break
