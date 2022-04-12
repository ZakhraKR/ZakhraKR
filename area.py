class Square:
    def __init__(self,side):
        self.side=side
        if side<=0:
            raise Exception('Basis (side) of square must be positive numbers! ')
    def area(self):
        return self.side*self.side
a=int(input("Enter side of square: "))
obj=Square(a)
print("Area of square:",obj.area())
 
print()