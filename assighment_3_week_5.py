string = input("Enter a string with numbers, symbols, capital and small letters : ")
capital = 0
small = 0
numbers = 0
other = 0
for letter in string:
    if letter.isupper():
        capital += 1
    elif letter.islower():
        small += 1
    elif letter.isdigit():
        numbers += 1
    else:
        other += 1
print("- Capital letters :", capital)
print("- Small letters :", small)
print("- Numbers :",numbers )
print("- Other characters :", other)