class Student:
    def __init__(self):
        self.name = "Shobana"
        self.__age = 21
obj=Student()
print(obj.name)
print(obj.__age)
