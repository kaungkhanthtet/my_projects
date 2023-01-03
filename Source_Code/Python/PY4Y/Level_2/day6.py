# class Person:
#     def __init__(self,name,age,hair_color,height,weight):
#         self.name = name
#         self.age = age
#         self.hair_color = hair_color
#         self.height = height
#         self.weight = weight

# p1 = Person("John", 36, "red", "180cm", "160 lb")
# p2 = Person("Kevin", 14, "black", "174cm", "185 lb" )
# p3 = Person("Max", 15, "Gray", "188 cm", "211 lb")
# print(p1.name, p1.age, p1.hair_color, p1.height, p2.weight, end = " ")
# print()
# print(p2.name, p2.age, p2.hair_color, p2.height, p2.weight, end = " ")
# print()
# print(p3.name, p3.age, p3.hair_color, p3.height, p3.weight, end = " ")
# print()




print("**********")

# class Person:
#     def __init__(user,name,age,hair_color,height,weight):
#         user.name = name
#         user.age = age
#         user.hair_color = hair_color
#         user.height = height
#         user.weight = weight

# p1 = Person("John", 36, "red", "180cm", "160 lb")
# p2 = Person("Kevin", 14, "black", "174cm", "185 lb" )
# p3 = Person("Max", 15, "Gray", "188 cm", "211 lb")
# print(p1.name, p1.age, p1.hair_color, p1.height, p2.weight, end = " ")
# print()
# print(p2.name, p2.age, p2.hair_color, p2.height, p2.weight, end = " ")
# print()
# print(p3.name, p3.age, p3.hair_color, p3.height, p3.weight, end = " ")
# print()

print("**********")

# class Cat:
#     #Constructor
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

#     #Instance methods
#     def speak (self):
#         print(self.name, "whose age is", self.age, "says: 'Meow'")

#     def drink (self):
#         print(self.name, "drinks some milk")

# #Creation of two objects of a Cat class

# romeo = Cat ("Romeo", 3)
# juliet = Cat ("Juliet", 2)

# romeo.speak()
# romeo.drink()

# juliet.speak()
# juliet.drink()

print("**********")
#Exercise

class Student:
    def __init__(self,english,math,science):
        self.english = english
        self.math = math
        self.science = science
    

    def calculate (self):
        total_mark = self.english + self.math + self.science
        if total_mark >= 240:
            print("Go to class A")
        elif total_mark<240 and total_mark>180:
            print("Go to class B")
        elif total_mark<180 and total_mark>120:
            print("Go to class C")
        else:
            print("Fail")



s1 = Student (100,100,100)
s2 = Student (80,80,70)
s3 = Student (40,80,50)
s4 = Student (40,30,30)

s1.calculate()
s2.calculate()
s3.calculate()
s4.calculate()

# print("**********")





