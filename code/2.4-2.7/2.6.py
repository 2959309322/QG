# 2.6

import math
class Shape:
    def __init__(self):
        self.area = 0
        pass

    def calc_area(self):
        pass


class Circle(Shape):
    """
    data格式 [r]
    """
    def __init__(self,data:list):
        super().__init__()
        self.r = data[0]

    def calc_area(self):
        self.area = math.pi*self.r**2
        return self.area

class Rectangle(Shape):
    """
    data格式[width,height]
    """
    def __init__(self,data:list):
        super().__init__()
        self.width = data[0]
        self.height = data[1]

    def calc_area(self):
        self.area = self.width*self.height
        return self.area

#把类封装到一个文件的时候要import ..
#这里在同一个文件里比较方便

cir = Circle([1])
print(cir.calc_area())
rec = Rectangle([1,2])
print(rec.calc_area())
