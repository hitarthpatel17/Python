a = int(input("Enter First Number : ")) 
b = int(input("Enter Second Number : "))

i = 1 
gcd = 0 
while i <= a and i<=b: 
    if a % i == 0 and b % i == 0:
        gcd = i 
        i+=1 
print(f"The GCD is {gcd}")