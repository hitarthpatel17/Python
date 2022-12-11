print("\n To implement stack using list \n") 
stack = [] 
def push(n): 
        print("\n Push Operation \n") 
        for i in range(n): 
            element = int(input("\nEnter element : ")) 
            stack.append(element) 
        print("Elements inserted\n") 
def pop(): 
        print("\n Pop Operation \n") 
        print("Popped element : ",stack.pop()) 
def peep(i): 
        print("\n Peep Operation \n") 
        print(f"element at position {i} is {stack[i-1]}") 
def change(i): 
        print("\n Change Operation \n") 
        stack[i-1] = int(input("Enter New Element : ")) 
def display(): 
        print("\n Stack elements \n") 
        print(stack) 
flag = 'y' 
while flag == 'y': 
            print("Enter 1 for Push") 
            print("enter 2 for Pop") 
            print("Enter 3 for Peep") 
            print("Enter 4 for Change") 
            try: 
                choice = int(input("\nEnter Your choice : ")) 
            except ValueError: 
                print("Please enter integer values\n") 
            if choice == 1: 
                n = int(input("Enter the number of elements in stack : ")) 
                push(n) 
            elif choice == 2: 
                pop() 
            elif choice == 3: 
                i = int(input("Enter the position to get the value : ")) 
                peep(i) 
            elif choice == 4: 
                i = int(input("Enter the position to change the value : ")) 
                change(i) 
            else: 
                print("Enter right choice please\n") 
            display() 
            flag = input("Do you want to continue ? y/n : ")