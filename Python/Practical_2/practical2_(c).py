print("\nDevelop a python program to print even numbers in list \n")
list1 = []
n =int(input("Enter number of elements in list : "))
for i in range(n):
    list1.append(int(input(f"Enter element {i+1} : ")))
print("\nEven elements in list")
for i in list1:
    if i % 2 == 0:
        print(f"{i}")
