a=[]
n = int(input("Enter number of elements:"))
for i in range(1,n+1):
    b= int(input("Enter Element:"))
    a.append(b)
    a.sort()
print("largest elements is:",a[n-1])