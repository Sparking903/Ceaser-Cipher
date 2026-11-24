from pathlib import Path
wordFile = Path(__file__).with_name("words.txt")

wordsList = []
with wordFile.open() as f:
    for word in f:
        wordsList.append(word.strip().lower())

def compareList(listToTest, index):
    possibleSolves = []
    for item in listToTest:
        for comparedWordInList in wordsList:
            if(((item.split())[index]).strip().lower() == comparedWordInList.strip()): possibleSolves.append(item); break
    if (len(possibleSolves) > 1 and len(listToTest[0].split()) > index + 1): possibleSolves = compareList(possibleSolves, index + 1)
        


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
         
elif EoD == "E":
    Msg = input("Please enter the message you desire to be rotated: ")
    while(True):
        RoT = input("Please enter the rotational value for encoding: ")
        try:
            RoT = int(RoT)
        except: print("Please enter a proper Int value")
        else: break
    RoT = abs(RoT)
    tempText = Msg.split(" ")
    decodedText = ""
    decodedPossiblities = []
    for word in tempText:
        for letter in word:
            if (ord(letter) >= 97):
                if (ord(letter) + RoT > 122):       
                    decodedText += chr((ord(letter) + RoT) - 26) 
                else: decodedText += chr((ord(letter) + RoT))
            elif(ord(letter) >= 65 and ord(letter) < 97):
                if (ord(letter) + RoT > 90):
                    decodedText += chr((ord(letter) + RoT) - 26) 
                else: decodedText += chr((ord(letter) + RoT))
        decodedText += " "
    print(decodedText)
    


