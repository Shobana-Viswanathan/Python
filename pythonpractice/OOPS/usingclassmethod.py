class Circle:
    def __init__(self, radius=1.0, color='red'):
        self.radius = radius
        self.color = color
    @classmethod
    def withRadius(cls,radius):
        return cls(radius)
    @classmethod
    def withRadiusandColor(cls,radius,color):
        return cls(radius,color)
    def getRadius(self):
        return self.radius
    def getColor(self):
        return self.color
    def setRadius(self, radius):
        self.radius=radius
    def setColor(self, color):
        self.color = color
    def getArea(self):
        return 3.14159*self.radius*self.radius
    def __str__(self):
        return f"Circle[radius={self.radius}, color={self.color}]"
    
circle1 = Circle()
print(circle1)

circle2 = Circle.withRadius(2.5)
print(circle2)

circle3 = Circle.withRadiusandColor(3.5, 'Blue')
print(circle3)