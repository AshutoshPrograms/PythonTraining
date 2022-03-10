oddNum = 0
evenNum = 0
for num in range(1,10):
    if num% 2 == 0:
        evenNum += 1
    else:
        oddNum += 1
print("Number of even numbers :",evenNum)
print("Number of odd numbers :",oddNum)
