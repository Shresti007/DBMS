class Vehicle:
    def __init__(self, driver, wheels,seats):
        self.driver =driver
        self.wheels = wheels
        self.seats = seats

    def __str__(self):
        return f"{self.driver} is buying {self.wheels} wheel car having {self.seats}, it is also called as SUV."


veh_1 = Vehicle("Surya", 4, 4)
print(veh_1)