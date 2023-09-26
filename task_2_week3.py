
try:
    score = int(input("Enter the score: "))
   
    if score >= 90 : 
       print("Grade is A")
    elif score >= 80 : 
       print("Grade is B")
    elif score >= 70 : 
       print("Grade is C")
    elif score >= 60 : 
       print("Grade is D")
    elif score < 60 : 
       print("Grade is F")
except ValueError:
    print("Error, please enter numeric input between 0 and 100") 

    



