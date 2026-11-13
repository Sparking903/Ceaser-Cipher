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
            #print(decodedText)
            decodedText += " "
        decodedPossiblities.append(decodedText.strip())

    print(decodedPossiblities)
    print(tempText)
else: print((chr)(ord(' ') + 1)) 