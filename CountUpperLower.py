stringVal = "The quick Brow Fox"
countUpper = 0
countLower = 0
stringVal = stringVal.replace(" ", "")
for charVal in stringVal:
    if str(charVal).islower():
        countLower += 1
    else:
        countUpper += 1
    
print("No. of Upper case characters :", countUpper) 
print("No. of Lower case characters :", countLower) 
