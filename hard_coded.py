def temparature(a,b,c,time):
    temp = a*(time**2) + b*time + c
    return temp

a = 0.1
b = 2
c = 10
time = 5

temp = temparature(a,b,c,time)

print("Temperature for hardcoded coefficients at time", time ,"hours is:-",temp)