print("Develop a Python Program to Understand Working of Exception Handling")
class MyException(Exception):
    def __init__(self, arg):
        self.msg = arg

def check_dict(dict1):
    for k,v in dict1.items():
        print(f"Name : {k} Balance : {v}")
        if v < 2000.00:
            raise MyException(f"\nhello {k}, Balance is not sufficient.")

no = int(input("Enter Number of Employees : "))
dict1 = dict()
for i in range(no):
    key = input("Enter Your name : ")
    dict1[key] = int(input("Enter the amount of salary : "))

try:
    check_dict(dict1)
except MyException as me:
    print(me.msg)