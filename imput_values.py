def temparature(a,b,c,time):
    temp = a*(time**2) + b*time + c
    return temp

a = float(input('enter the value of a '))
b = float(input('enter the value of b '))
c = float(input('enter the value of c '))
time = float(input("Enter the time  "))

temp = temparature(a,b,c,time)
print("Temperature for the coefficients at time", time ,"hours is:-",temp)