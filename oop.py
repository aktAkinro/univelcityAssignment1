# class  DjangoStudent():
#     def __init__(self, name,  laptop):
#         self.name = name
#         self.computer = laptop

# mystudent = DjangoStudent("Tunde","Acer")
# print(mystudent.computer)

# class  BankApp():
#     def __init__(self, name,  balance):
#         self.name = name
#         self.balance = balance

#     def deposit(self, amount):
#         self.balance += amount

#         return self.balance

#     def name_tolower(self):
#         self.name = self.name.lower()
#         return self.name
    

# customer1 = BankApp("Tunde",105.45)
# print(customer1.name_tolower())
# print(customer1.deposit(1000))
            


# class  Vehicle():
#     def __init__(self, max_speed,  mileage):
#         self.speed = max_speed
#         self.mileage = mileage

#     def get_accelation (self, time):
#         c = self.mileage*2 / time**2
#         return c



# car = Vehicle(180,12.5)
# c = car.get_accelation(12)
# print(c)
# print(car.speed)
# print(car.mileage)


        

# inheritance


class Employee():
    def __init__(self, name, salary,designation):
        self.name = name
        self.salary = salary
        self.designation = designation

    @property #allows see method as an attribute
    def bonus(self):
        bo = self.salary * 0.1
        return self.salary + bo
a =Employee("Tosin", 10, "Q/A")
print(a.bonus())

class Supervisors(Employee):
    def __init__(self, name, salary, designation):
        super().__init__(name, salary, designation)

    def bonus(self): # without this line the supervisor would inherit original 10 percent bonus
        return self.salary + (self.salary * 0.17)
b = Supervisors("Tunde", 100000000000, "Supervise")
print(b.bonus())

    
# property method
# allows see method as an attribute using "@property". it becomes an attributte but is still a function



