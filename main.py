def compareList(listToTest, index):
    possibleSolves = []
    print(listToTest) #Test print
    wordFile = open("words.txt")
    wordsList = []
    for word in wordFile:
        wordsList.append(word.strip().lower())
    for item in listToTest:
        print(item.split()[index]) #Test print
        for comparedWordInList in wordsList:
            if(((item.split())[index]).strip().lower() == comparedWordInList.strip()): possibleSolves.append(item)
    print(possibleSolves) #Test print
    print(len(listToTest[0].split()))
    if (len(possibleSolves) > 1 and len(listToTest[0].split()) > index + 1): possibleSolves = compareList(possibleSolves, index + 1)
    return possibleSolves
        


EoD = input("Enter E for encoding. Enter D for Decoding: ")
if EoD == "D":
    TestedText = input("Enter the text to be decoded: ")
    tempText = TestedText.split(" ")
    decodedText = ""
    decodedPossiblities = []
    for i in range(1,26):
        decodedText = ""
        for word in tempText:
            for letter in word:
                if (ord(letter) >= 97):
                    if (ord(letter) + i > 122):       
                        decodedText += chr((ord(letter) + i) - 26) 
                    else: decodedText += chr((ord(letter) + i))
                else:
                    if (ord(letter) + i > 90):       
                        decodedText += chr((ord(letter) + i) - 26) 
                    else: decodedText += chr((ord(letter) + i))

            decodedText += " "
        decodedPossiblities.append(decodedText.strip())

    print(compareList(decodedPossiblities, 0))
else: print((chr)(ord(' ') + 1)) 

