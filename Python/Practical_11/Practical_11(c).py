class Square:
    def __init__(self, x = 0):
        self.x = x
    def area(self):
        print(f"Area Of Square is {self.x*self.x}")
class Rectangle(Square):
    def __init__(self, x = 0, y = 0):
        super().__init__(x)
        self.y = y
    def area(self):
        super().area()
        print(f"Area Of Rectangle is {self.x * self.y}")
x = int(input("Enter x : "))
y = int(input("Enter y : "))
r = Rectangle(x,y)
r.area()
