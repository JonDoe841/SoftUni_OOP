# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def eat(self):
#         return "eating"
#
#
# class Teacher(Person):
#     def __init__(self, name, age, salary):
#         super().__init__(name, age)
#         self.salary = salary
#
#
#
# t  = Teacher("test", 40, 1000)
# print(t.eat())
#
# # class Fireman:
# #     def __init__(self, name, age, salary, equipment):
# #         self.name = name
# #         self.age = age
# #         self.salary = salary
# #         self.equipment = equipment
# #
# #     def eat(self):
# #         return "eating"


class Person:
    def __init__(self, first_name: str, last_name: str):
        if  len(first_name) < 2:
            raise ValueError("Person can be instantiated with name less than 2 chars")

        self.first_name = first_name
        self.last_name = last_name



    def greet(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return "i am a person"


class Student(Person):
    def __init__(self, first_name, last_name, fac_number):
        super().__init__(first_name, last_name)
        self.fac_number = fac_number

    def greet(self):
        return super().greet() + f" {self.fac_number}"

    def __str__(self):
        return super().__str__() + " but also a student"


s = Student("Test", "testov", "123")
print(s)