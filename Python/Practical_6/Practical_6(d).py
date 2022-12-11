print("\nWrite a python program to perform the Binary Search\n")
list1 = [] 
def Binary_Search(low, high, e): 
    if high >= low: 
        middle = (high + low) // 2 
        if list1[middle] == e: 
            return middle 
        elif list1[middle] > e: 
            return Binary_Search(low, middle-1, e) 
        else: 
            return Binary_Search(middle+1, high, e) 
    else: 
        return -1 
n = int(input("\nEnter the number of elemets in ascending manner : ")) 
for i in range(n): 
    list1.append(int(input("Enter element : "))) 
    flag = 'y' 
while flag == 'y': 
    e = int(input("\nEnter the element that you want to search : ")) 
    low = 0 
    high = n-1 
    result = Binary_Search(low, high, e) 
    if result != -1: 
        print("\nThe position of the given element is ",result) 
    else: 
        print("\nElement is not present ")
    flag = input("\nDo you want to search another element ? y/n : ") 
