# class Student:
# #
# #
# #     def __init__(self):
# #         self.height = 160  #конструктор, инициализация полей !!        self.height = 160   #self - посилання на самого себе !!
# #         print("I am alive!")
# #
# #
# # first_student = Student()


# class Student:
#     def __init__(self, height=160):  # параметр по умолчанию
#         self.height = height
#
#
# nick = Student(height=160)
# kate = Student(height=170)
# print(nick.height)
# print(kate.height)

# class Student:
#
#     def __init__(self):
#         self.height = 170
#
#     def printer(self):
#             print(self.height)
#
# student1 = Student()
# student1.printer()

class Car:

    def __init__(self, wheels, frame):
        self.wheels = wheels
        self.frame = frame


car = Car(4, "metal")


print(f"{car.wheels} wheels")
print(f"{car.frame} frame")
