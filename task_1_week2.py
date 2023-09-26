#x = float(input(" work hours:")) 
#y = float(input("salary rate:"))
#print("salary:" + str(x*y) + "$")


#z = float(input("Celsius:"))
#y = z * 9 / 5 + 32
#print("Fahrenheit:" + str(b))


a = int(input("enter seconds:"))
n = a//3600 
z = n%3600
f = z//60
d = z%60

print(str(a) + " seconds is " + str(n)  + " hours " + str(z) + " minutes " + str(d) + " a " )
