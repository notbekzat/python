while True:
    string1 = input("Enter a string : ")
    if string1 == 'done':
        print("Bye Bye see you")
        break
    symbols = [',','.',':','!','?']
    string2 = ""
    for letter in string1:
        if letter not in symbols:
            string2 += letter
    capital = string2.upper()
    print(capital)