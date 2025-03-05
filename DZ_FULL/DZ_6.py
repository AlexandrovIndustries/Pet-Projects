#1 Students 
"""class Student:
    def __init__(self, name="Ivan", age=18, groupNumber="10A"):
        self.name = name
        self.age = age
        self.groupNumber = groupNumber

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def getGroupNumber(self):
        return self.groupNumber

    def setNameAge(self, name, age):
        self.name = name
        self.age = age

    def setGroupNumber(self, groupNumber):
        self.groupNumber = groupNumber

student1 = Student()
student2 = Student()
student3 = Student()
student4 = Student()
student5 = Student()

student1.setNameAge("Anna", 19)
student1.setGroupNumber("11B")

student2.setNameAge("Petr", 20)
student2.setGroupNumber("12C")

student3.setNameAge("Maria", 18)
student3.setGroupNumber("10A")

student4.setNameAge("Alex", 21)
student4.setGroupNumber("13D")

student5.setNameAge("Olga", 22)
student5.setGroupNumber("14E")

students = [student1, student2, student3, student4, student5]
for i, student in enumerate(students, 1):
    print(f"Student {i}:")
    print(f"Name: {student.getName()}")
    print(f"Age: {student.getAge()}")
    print(f"Group Number: {student.getGroupNumber()}")
    print()

"""
#2 Car

class Car:
    def __init__(self, color="неизвестно", type="неизвестно", year="неизвестно"):
        self.color = color
        self.type = type    
        self.year = year  

    def start(self):
        print("Автомобиль заведен")

    def stop(self):
        print("Автомобиль заглушен")

    def set_year(self, year):
        self.year = year
        print(f"Год выпуска автомобиля - {self.year}")

    def set_type(self, type):
        self.type = type
        print(f"Тип автомобиля - {self.type}")

    def set_color(self, color):
        self.color = color
        print(f"Цвет автомобиля - {self.color}")

    def get_info(self):
        return f"Автомобиль: {self.color}, {self.type}, {self.year} года выпуска"

car = Car()

car.set_color("Красный")
car.set_type("Седан")
car.set_year(2020)

car.start()
car.stop()

print(car.get_info())