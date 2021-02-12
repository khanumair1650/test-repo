# day 1  EXPERT PYTHON                                                          #1
# OOP
# 1.inheritance 2.polymorphism 3.abstraction 4.encapsulation

# ENCAPSULATION PROGRAM

# creating class   #SET #GET METHOD

class Student:

    def __init__(self, name, age=0):  # initialization_function
        self.name = name
        self.age = age  # __ make our data private

    def display(self):
        print(self.name)
        print(self.age)
    def getAge(self):
        print(self.age)
    def setAge(self,age):
        self.age= age


student = Student(' UMAIR ', 19)
student.display()

student.setAge(90)
student.getAge()