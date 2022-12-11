aasci = 65 
for i in range(6):
    # print("this is i ",i) 
    for j in range(i):
        print(chr(aasci),end=" ") 
        aasci += 1
    print("\n")