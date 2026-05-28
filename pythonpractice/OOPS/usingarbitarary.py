class Circle:
    def __init__(self, *args):

        if len(args) == 0:
            self.radius = 1.0
            self.color = "red"

        elif len(args) == 1:
            self.radius = args[0]
            self.color = "red"

        elif len(args) == 2:
            self.radius = args[0]
            self.color = args[1]

        else:
            raise ValueError("Too many arguments")

    def getRadius(self):
        return self.radius

    def getColor(self):
        return self.color

    def setRadius(self, radius):
        self.radius = radius

    def setColor(self, color):
        self.color = color

    def getArea(self):
        return 3.14159 * self.radius * self.radius

    def __str__(self):
        return f"Circle[radius={self.radius}, color={self.color}]"


circle1 = Circle()
print(circle1)

circle2 = Circle(2.5)
print(circle2)

circle3 = Circle(3.5, 'Blue')
print(circle3)