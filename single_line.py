def temparature(a,b,c,time):
    temp = a*(time**2) + b*time + c
    return temp

with open('data_single_line.txt' , 'r') as f:
    lines = f.readline()
    print(lines)
    a,b,c,time = map(float,lines.split())
    temp = temparature(a,b,c,time)
    print("Temperature for the coefficients at time", time ,"hours is:-",temp)