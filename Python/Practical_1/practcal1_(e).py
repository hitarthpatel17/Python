a = int(input("Enter lower Limit : ")) 
b = int(input("Enter upper Limit : ")) 
for num in range(a,b + 1):
    if num > 1:
        for i in range(2,num): 
            if (num % i) == 0:
                break 
        else:
            print(num)