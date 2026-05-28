class Student():
    def __init__(self):
        self._name="Shobana"
    def _funName(self):
        return "Method here"
class Subjet(Student):
    pass
obj=Student()
obj1=Subjet()
print(obj._name)
print(obj._funName())
print(obj1._name)
print(obj1._funName())