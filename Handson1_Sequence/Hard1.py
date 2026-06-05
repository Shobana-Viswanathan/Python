radius= float(input("Enter the radius of the circle: "))
angle= float(input("Enter the angle in degress (for sector area): "))
pi= 3.14159
diameter = 2 * radius
circumference = 2 * pi * radius
area= (pi * radius * radius ) * (angle / 360)
arc = (circumference) * (angle / 360 )
print("Radius: ",radius)
print("Diameter: ",diameter)
print("Circumference: ",circumference)
print("Sector Area for",angle,"degrees:",area)
print("Arc Length for",angle,"degress:",arc)
