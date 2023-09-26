try:
    hours = int(input("Enter the hours of work: "))
    rate = float(input("Enter the rate: "))
    if hours <= 40 : 
        pay = hours * rate 
    else :
        pay = rate * 40 +((hours  - 40 ) * 1.5 * rate)
    print("payment: " , pay)
except ValueError:
    print("Error, please enter numeric input") 

    
