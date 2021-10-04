# class Employee(object):
#     """Medls real life employees"""
#     def __init__(self, employee_name):
#         self.employee_name = employee_name
#
#     def calculate_wage(self, hours):
#         self.hours = hours
#         return hours * 20
#
#
# class PartTimeEmployee(Employee):
#     """Models real life part time employees"""
#     def calculate_wage(self, hours):
#         self.hours = hours
#         return hours * 12
#
# jørgen = Employee("Jørgen")
# print(f"Jørgen tjener: {jørgen.calculate_wage(10)}")
#
# niller = PartTimeEmployee("Niller")
# print(f"Niller tjener: {niller.calculate_wage(10)}")


class Car:
    condition = "new"

    def __init__(self, model, color, mpg):
        self.model = model
        self.color = color
        self.mpg = mpg

    def __str__(self):
        return "This is a: " + str(self.color) + " " + str(self.model) + " with " + str(self.mpg) + " mpg."


my_car = Car("DeLorean", "Silver", 88)
print(f"The condition is: {my_car.condition}")
print(f"The condition is: {my_car.model}")
print(f"The condition is: {my_car.color}")
print(f"The condition is: {my_car.mpg}")
print(my_car.__str__())