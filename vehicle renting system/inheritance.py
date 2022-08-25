# Inheritance makes use of code for Children class that has been already written for Parent class. For example,
# some attributes of vehicle class is same as car, bus and truck class. Driver Name, Number of Wheels etc. attributes
# are same in all the classes. Vehicle is a parent class and Car, bus and truck are children classes. In OOO,
# it means a class inherits attributes and behavior methods from its parent class. Create a parent class Vehicle and
# using its attributes for child class Vehicle. In the program below, we don't need to specify attributes of class
# cab. It inherits from vehicle.


class Vehicle:
    def __init__(self, driver, wheels, seats):
        self.driver = driver
        self.noofwheels = wheels
        self.noofseats = seats


class Cab(Vehicle):
    pass


cab1 = Cab("Surya", 4, 2)
print(cab1.driver)


# How to change class variable of subclass Vehicle
class Vehicle:
    minimumrate = 50

    def __init__(self, driver, wheels, seats):
        self.driver = driver
        self.noofwheels = wheels
        self.noofseats = seats


class Cab(Vehicle):
    minimumrate = 75


print(Vehicle.minimumrate)
print(Cab.minimumrate)


# How to have child class with more parameters than our parent class In this example, we have two classes Cab and Bus
# which have many attributes which are similar but there are a few which are unique to class. To solve this,
# we have created a parent class named Vehicle which contains common attributes and method.

class Vehicle:
    minimumrate = 50

    def __init__(self, driver, wheels, seats, kms, bill):
        self.driver = driver
        self.noofwheels = wheels
        self.noofseats = seats
        self.running = kms
        self.bill = bill

    def rateperkm(self):
        return self.bill / self.running


class Cab(Vehicle):
    minimumrate = 75

    def __init__(self, driver, wheels, seats, kms, bill, cabtype):
        super().__init__(driver, wheels, seats, kms, bill)
        self.category = cabtype

class Bus(Vehicle):
    minimumrate = 60

    def __init__(self, driver, wheels, seats, kms, bill, color):
        super().__init__( driver, wheels, seats, kms, bill)
        self.color = color


Cab1 = Cab("chandana", 4, 4, 300, 2000, "sedan")
Bus1 = Bus("Surya", 6, 40, 5000, 20000, "red")
print(Cab1.category)
print(Bus1.color)

