string = input("Enter the string : ")
print("Input string =", string)
letter = len(string) - 1
while letter >= 0:
    print(string[letter])
    letter -= 1