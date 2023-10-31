while True:
    str1 = input("Please enter two words : ")
    if str1 == 'done':
        print('-- bye bye')
        break
    elif str1 == '':
         print('-- bye bye')
         break
    words = str1.split()
    if len(words) != 2:
        str1 = input("Enter two words : ")
    else:
        word1, word2 = words
        if word1 < word2:
            print(f"{word1} comes first")
        elif word2 < word1:
            print(f"{word2} comes first")