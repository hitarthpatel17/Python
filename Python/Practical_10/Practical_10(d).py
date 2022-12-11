# import matplotlib.pyplot as plt
# fig = plt.figure()
# ax = fig.add_axes([0,0,1,1])
# languages = ['c','c++','java','python','c#']
# students = [23,17,35,34,15]
# ax.bar(languages, students)
# plt.show()#!/usr/bin/python3

class Employee:
   'Common base class for all employees'
   empCount = 0

   def __init__(self, name,department,salary):
      self.name = name
      self.department=department
      self.salary = salary
      Employee.empCount += 1
   
   def displayCount(self):
     print ("Total Employee %d" % Employee.empCount)

   def displayEmployee(self):
      print ("Name : ", self.name,  ", Department:",self.department, ", Salary: ", self.salary)


#This would create first object of Employee class"
emp1 = Employee("Zara","CE" ,2000)
#This would create second object of Employee class"
emp2 = Employee("Manni","IT",5000)
emp1.displayEmployee()
emp2.displayEmployee()
print ("Total Employee %d" % Employee.empCount)