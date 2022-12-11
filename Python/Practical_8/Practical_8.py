print("\nTo write a python program to create, slice, change, delete and index elements using tuple \n")
list1 = []
tup1 = None
n = int(input("Enter number to create a tuple : "))
for i in range(n):
 list1.append(input("Enter Element : "))
tup1 = tuple(list1) 
print("\nTuple created \n") 
def Slice():
 print("\nSlicing of Tuple\n")
 length = len(tup1)
 print(f"The length of tuple is {length} \n So kindly enter limits in range 0 to {length-1}")
 n1 = int(input("Enter first limit : "))
 n2 = int(input("Enter second limit : "))
 if n1 >=0 and n2 <= length:
    print("Slice is : ")
    print(tup1[n1:n2+1])
 
def Change():
 print("\n:( OOPs ! sorry Tuple is immutable \nThat's why it is not possible to change the tuple\n")
def Delete():
 global tup1
 print("\nIt is not possible to change the single element in tuple")
 c = input("\nDo you want to delete the tuple ? y/n : ")
 if c == 'y':
    del tup1
    print("Tuple is deleted")
def Indexing():
 length = len(tup1)
 i = int(input(f"Enter position to get value at that position(between 0 to {length-1}) : "))
 print(f"The value at position {i} is {tup1[i]} \n ")
def display():
 print("\n\nTuple is : \n")
 print(f"{tup1}\n")
flag = 'y'
while flag == 'y':
 print("enter 1 for Slicing")
 print("Enter 2 for Chnage")
 print("Enter 3 for Delete")
 print("Enter 4 for get the value(indexing)")
 print("Enter 5 for displaying")
 try:
    choice = int(input("\nEnter Your choice : "))
 except ValueError:
    print("Please enter integer values\n")
 
 if choice == 1:
    Slice()
 elif choice == 2:
    Change()
 elif choice == 3:
    Delete()
 elif choice == 4:
    Indexing()
 
 elif choice == 5:
    print("After deleting the tuple will not be displayed and error will occur")
    display() 
 
 else:
    print("Enter right choice please\n") 
 flag = input("\nDo you want to continue ? y/n : ")