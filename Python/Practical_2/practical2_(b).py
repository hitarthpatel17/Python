print("\nTo write a program merge two lists\n\n")
list1 = []
list2 = []
n = int(input("Enter number of elements for list1 : "))
for i in range(n):
    list1.append(input(f"Enter element of number {i+1} : "))
n = int(input("\nEnter number of elements for list2 : "))
for i in range(n):
    list1.append(input(f"Enter element of number {i+1} : "))
list1.extend(list2)
print("\nMerged list is : ")
print(list1)