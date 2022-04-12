class Square:
    def __init__(self,side):
        self.side=side
        if side<=0:
            raise Exception('Basis (side) of square must be positive numbers! ')
    def perimeter(self):
        return self.side*4
a=int(input("Enter side of square: "))
obj=Square(a)
print("Perimeter of square:",obj.perimeter())
 
print()