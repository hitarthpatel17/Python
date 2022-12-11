print("\nWrite a python program to perform the Linear Search\n") 
list1 = []
def Linear_Search(n, e): 
    for i in range(n): 
        if list1[i] == e: 
            print("\nThe element is at position ",i) 
    return 
n = int(input("\nEnter the number of elemets : ")) 
for i in range(n): 
    list1.append(int(input("Enter element : "))) 
    flag = 'y' 
while flag == 'y': 
    e = int(input("\nEnter the element that you want to search : ")) 
    Linear_Search(n, e) 
    flag = input("\nDo you want to search another element ? y/n : ")