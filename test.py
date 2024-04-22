

import math

def circle( radius):
    return round(math.pi * radius **2, 2)

circle_1=circle(4)
print(circle_1)

   
class MyClass:
    def __init__(self, x):
        self.x = x

    def print_x(self):
        print(self.x)

# Create an instance of MyClass
obj = MyClass(5)

# Call the print_x method of the instance
obj.print_x()  # This will print: 5


class SampleClass:
    def __init__(self, ):
        pass