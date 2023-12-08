def temparature(a,b,c,time):
    temp = a*(time**2) + b*time + c
    return temp

with open('data_multiple_line.txt' , 'r') as f:
    lines = f.readlines()
     
    i = 0
    while(i<len(lines)):
        a,b,c,time = map(float,lines[i].split())
        temp = temparature(a,b,c,time)
        print("Temperature for the coefficients at time", time ,"hours is:-",temp)
        i = i+1
    
        
