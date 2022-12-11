class Student():
    def __init__(self, name = "", branch = ""):
        self.name = name
        self.branch = branch
    def display(self):
        print(f"Hi {self.name}")
        print(f"Your branch is : {self.branch}")
s1 = Student()
s1.display()
print("..................................................")
name = input("Enter Name Your : ")
branch = input("Enter Branch : ")
s2 = Student(name, branch)
s2.display()
print("..................................................")
