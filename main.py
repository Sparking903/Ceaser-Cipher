wordFile = open("words.txt")
wordsList = []
for word in wordFile:
    wordsList.append(word.strip().lower())

def compareList(listToTest, index):
    possibleSolves = []
    #print(listToTest) #Test print
    for item in listToTest:
        #print(item.split()[index]) #Test print
        for comparedWordInList in wordsList:
            if(((item.split())[index]).strip().lower() == comparedWordInList.strip()): possibleSolves.append(item); break
    #print(possibleSolves) #Test print
    if (len(possibleSolves) > 1 and len(listToTest[0].split()) > index + 1): possibleSolves = compareList(possibleSolves, index + 1)# and print("Next Call")
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
                elif(ord(letter) >= 65 and ord(letter) < 97):
                    if (ord(letter) + i > 90):
                        decodedText += chr((ord(letter) + i) - 26) 
                    else: decodedText += chr((ord(letter) + i))

            decodedText += " "
        decodedPossiblities.append(decodedText.strip())
    finalList = compareList(decodedPossiblities, 0)
    for possiblity in finalList:
        #print(possiblity)
        for index, char in enumerate(TestedText):
            tempIndex = 0
            if (ord(char) <= 64 and ord(char) != 32 ): possiblity = possiblity[:index - tempIndex] + char + possiblity[index - tempIndex:]
        print(possiblity)
            
        
else: print((chr)(ord(' ') + 1)) 

