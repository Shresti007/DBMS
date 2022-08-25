class Cab:
    numofcabs = 0
    numpassngrs = 0

    def __init__(self, driver, km, places, pay, passengers):
        self.driver = driver
        self.km = km
        self.place = places
        self.pay = pay
        Cab.numofcabs = Cab.numofcabs + 1
        Cab.numpassngrs = Cab.numpassngrs + passengers

    def rateperkm(self):
        return self.bil / self.running

    # class method
    @classmethod
    def noofcabs(cls):
        return cls.numofcabs

    @classmethod
    def avgnoofpassnegers(cls):
        return cls.numpassngrs / cls.numofcabs


cab1 = Cab("Ramesh", 80, ['Delhi', 'Noida'], 2200, 3)
cab2 = Cab("Suresh", 60, ['Gurgaon', 'Noida'], 1500, 1)
cab3 = Cab("Dave", 20, ['Gurgaon', 'Noida'], 680, 2)
print(cab1(self.driver))
