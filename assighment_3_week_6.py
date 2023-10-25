file = input("Enter a file name: ")
try:
    with open(file, 'x') as file:
        start = 0
        total_confidence = 0
        for line in file:
            if line.startswith("X_DSPAM_Confidence: "):
                confidence = float(line.split(":")[1])
                total_confidence += confidence
                start += 1
        if start > 0:
            average_confidence = total_confidence / start
            print("Average spam confidence: ", average_confidence)
except:
    print("File cant be opened : ", file)