import subprocess



EoD = input("Enter E for encoding. Enter D for Decoding: ")
if EoD == "D":
    TestedText = input("Enter the text to be decoded: ")
    tempText = TestedText.split(" ")
    for word in tempText:
        for letter in word:        
            print(letter)

    print(tempText)
else: print((chr)(ord(' ') + 1))