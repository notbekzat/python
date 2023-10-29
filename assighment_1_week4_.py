def grade(score):
    try:
        if 0 <= score <= 100:
            if 90 <= score <= 100:
                print("Your grade is A")
            elif 80 <= score < 90: 
                print("Your grade is B")   
            elif 70 <= score < 80: 
                print("Your grade is C")
            elif 60 <= score < 70:
                print("Your grade is D")
            else:
                print("Your grade is F")
        else: 
            print("Error, please enter numeric input between 0 and 100")
    except ValueError:
        print("Error, please enter numeric input between 0 and 100")
try:
    score = int(input('Enter the number: '))
    mark = grade(score)
except ValueError:
    print("Error, please enter numeric input between 0 and 100")