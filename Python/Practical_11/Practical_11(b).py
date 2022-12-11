# import datetime
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     @classmethod
#     def fromBirthYear(cls, name, year):
#         return cls(name, datetime.date.today().year - year)
#     @staticmethod
#     def isAdult(age):
#         return age>18
# print("\nUsing Constructor\n")
# name = input("Enter your name : ")
# age = int(input("Enter Your age : "))
# p1 = Person(name, age)
# print(f"The age of {p1.name} is {p1.age}")
# # static method for p1 object
# print(f"Is {p1.name} adult ? : {Person.isAdult(p1.age)}")
# print("\nUsing Class Method\n")
# name = input("Enter your name : ")
# age = int(input("Enter Your year of birth : "))
# p2 = Person.fromBirthYear(name, age)
# print(f"The age of {p2.name} is {p2.age}")
# #static method for p2 object 
# print(f"Is {p2.name} adult ? : {Person.isAdult(p2.age)}")
# class Parent:
#    def func1(self):
#         print("this is function 1")
# class Parent2:
#    def func2(self):
#         print("this is function 2")
# class Child(Parent , Parent2):
#     def func3(self):
#         print("this is function 3")
 
# ob = Child()
# ob.func1()
# ob.func2()
# ob.func3()
class Parent:
      def func1(self):
          print("this is function 1")
class Child(Parent):
      def func2(self):
          print("this is function 2")
class Child2(Child):
      def func3(self):
          print("this is function 3")
ob = Child2()
ob.func1()
ob.func2()
ob.func3()