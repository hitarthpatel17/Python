no = int(input("Enter a number : ")) 
t = no 
sum = 0 
while t > 0: 
    i = t % 10 
    sum = sum + i**3 
    t = t//10 
if no == sum:
    print("Number is Armstrong") 
else: 
    print("Number is not Armstrong")