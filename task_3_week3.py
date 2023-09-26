try:
    sum = 0
    count = 0
    avr = 0
    while True:
        number_inputs = input("Enter a number :  ")
        if number_inputs == "done":
            break
        else:
            sum += int(number_inputs)
            count += 1
            avr = sum/count 
    print("Sum of inputs: ", sum)
    print("number of inputs: ", count)
    print("Avarage of input numbers: ", avr)
except:
    print("end")
