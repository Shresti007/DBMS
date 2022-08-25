# python, there are three types of methods which are Instance, Class and Static Instance takes self as the first
# argument. They are also called Object or regular method. It's the same method which we have learnt so far in
# previous sections. Class takes cls as the first argument. cls refers to class. To access a class variable within a
# method, we use the @classmethod decorator, and pass the class to the methodS
# taticdoesn't take anything as the first argument. It has limited uses which are explained in the latter part of
# this article.


class Cab:
    # class attributes
    numofcabs = 0
    numpassngrs = 0

    def __init__(self, driver, km, places, pay, passengers):
        self.driver = driver
        self.km = km
        self.place = places
        self.pay = pay
        Cab.numofcabs = Cab.numofcabs + 1
        Cab.numpassngrs = Cab.numpassngrs + passengers

    # Here we are creating 3 methods : rateperkm, noofcabs, avgnoofpassengers.
    # First one is instance method and other two are class methods.
    # instance method
    def rateperkm(self):
        return self.pay / self.km

    # class method
    # @class method
    def noofcabs(cls):
        return cls.numofcabs

    @classmethod
    def avgnoofpassnegers(cls):
        return cls.numpassngrs / cls.numofcabs


cab1 = Cab("Ramesh", 80, ['Delhi', 'Noida'], 2200, 3)
cab2 = Cab("Suresh", 60, ['Gurgaon', 'Noida'], 1500, 1)
cab3 = Cab("Dave", 20, ['Gurgaon', 'Noida'], 680, 2)
print(cab1.rateperkm())
print(cab3.driver)
print(cab1.driver)
print(Cab.numpassngrs)
print(Cab.numofcabs)


class Car:
    @staticmethod
    def billvalidation(pay):
        return int(pay) > 0


print(Car.billvalidation(0.2))
