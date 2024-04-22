import math

class Circle:
    def __init__(self,radius):
        self.radius=radius
    
    def area(self):
        return round(math.pi * self.radius**2,2)


circle_1=Circle(4)

print(circle_1.radius)
print(circle_1.area())



class Namez:
    def __init__(self, name,price,age):
        self.name=name
        self.price=price
        self.age=age
    
    def worth(self):
        return self.age * self.price
    
    def __str__(self):
        return f"{self.name} is worth {self.worth()}"


person_1=Namez("baduu", 1000, 55)

person_2=Namez("arumyz", 2000, 33)

print(person_2)
print(person_1.name, "is worth", person_1.worth())