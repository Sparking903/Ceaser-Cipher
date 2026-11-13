import subprocess



EoD = input("Enter E for encoding. Enter D for Decoding: ")
if EoD == "D":
    TestedText = input("Enter the text to be decoded: ")
    tempText = []
    for i in range(1, 26):
        tempText = TestedText.split(" ")
        
        #print()

    print(tempText)
else: print((chr)(ord(' ') + 1))