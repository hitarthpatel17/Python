# class Parent:
#  def __init__(self, p = 0):
#     self.property = p
#  def display(self):
#     print(f"Parents property is {self.property}")
# class Children(Parent):
#  def __init__(self, p = 0, c = 0):
#     super().__init__(p)
#     self.property1 = c
#  def display(self):
#     super().display()
#     print(f"Children Property {self.property1 + self.property}")
# p = int(input("Enter Parents Property : "))
# c = int(input("Enter Children Property : "))
# c = Children(p,c)
# c.display()

# with open(r"src.txt", 'r') as fp:
#    lines = len(fp.readlines())
#    print('Total Number of lines:', lines)

# numbers = [1,2,3,4,5,1,4,5]
# Sum = sum(numbers)
# print(Sum)

x = int(input("Enter The Number: "))
print("factor of",x,"is:")
for i in range(1,x+1):
   if x%i==0:
      print(i)

# string = "01fe"
# if(string.count('0')+string.count('1')==len(string)):
#     print("Yes")
# else:
#     print("No")