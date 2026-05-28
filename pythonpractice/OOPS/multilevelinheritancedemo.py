class Student:
    def getStudentInfo(self):
        self.__rollno = input("Enter roll number:")
        self.__name=input("Enter name")
    def printStudentInfo(self):
        print("Roll Number: ",self.__rollno,"Name: ",self.__name)
class Marks(Student):
    def getMarks(self):
        self.getStudentInfo()
        self.__marks1 = float(input("Enter marks for subject 1: "))
        self.__marks2 = float(input("Enter marks for subject 2: "))
        self.__marks3 = float(input("Enter marks for subject 3: "))
    def printmarks(self):
        self.printStudentInfo()
        print("Marks1:",self.__marks1)
        print("Marks2:",self.__marks2)
        print("Marks3:",self.__marks3)

    def calcTotalMarks(self):
        return self.__marks1 + self.__marks2 + self.__marks3
    
class Result(Marks):
    def getResult(self):
        self.getMarks()
        self.__total=self.calcTotalMarks()
    def putResult(self):
        self.printmarks()
        print("Total Marks out of 300: ",self.__total)
obj=Result()
obj.getResult()
obj.getMarks()
