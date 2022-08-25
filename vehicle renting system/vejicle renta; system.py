import enum


class CarType(enum.Enum):
    HATCHBACK, SEDAN, SPORTS, LUXURY, UNKNOWN = 1, 2, 3, 4, 5


class MotorBike(enum.Enum):
    REGULAR, DIRTBIKE, CRUISERS, UNKNOWN = 1, 2, 3, 4


'''
Address class
'''


class Address:
    def __init__(self, street, city, state, zip, country):
        self.__street = street
        self.__city = city
        self.__state = state
        self.__zip = zip
        self.__country = country

    def __str__(self):
        return self.__street + "," + self.__city + "," + self.__state + "," + self.__zip + "," + self.__country

    def get_street(self):
        return self.__street

    def get_city(self):
        return self.__city

    def get_state(self):
        return self.__state

    def get_zip(self):
        return self.__zip

    def get_country(self):
        return self.__country


class Person:
    def __init__(self, name, address):
        self.__name = name
        self.__address = address

    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address


'''Customer class'''


class Customer(Person):

    def __init__(self, name, cust_address, email_id, phn_num):
        super().__init__(self, name, cust_address)
        self.__email_id = email_id
        self.__phn_num = phn_num

    def hire_vehicle(self, vehicle_type, vehicle_rental_system):
        print("[Customer : "+ super().get_name+"] hired a vehicle type : "+str(vehicle_type))

        vehicle_rental_system.book_vehicle(str(vehicle_type))

    def pick_vehicle(self, vehicle_type, vehicle):
        print("[Customer : " + super().get_name + "] pick a vehicle type : " + str(vehicle_type))
        print("[customer : vehicle initial meter reading : "+ str(vehicle.get_meter_reading()))
        vehicle.drive(500)

    def return_vehicle(self, vehicle_type, vehicle):
        print("[Customer : " + super().get_name + "] return the  vehicle type : " + str(vehicle_type))

    def payment(self, vehicle_type, vehicle, parking_attendant):
        print("[Customer : " + super().get_name + "] starting  the payment for   vehicle of type : " + str(vehicle_type))
        print("[Customer : vehicle final raeding "+ str(vehicle.get_meter_reading()))

        parking_attendant.inspect_vehicle(vehicle)
        parking_attendant.accept_cash(vehicle)
#vehicle class

class Vehicle:

    def __init__(self,make, total_km):
        self.__make= make
        self.__total_km = total_km

    def get_metre_reading(self):
        return self.__total_km

    def drive(self, distance):
        self.__total_km= self.__total_km + distance
        print("This vehicle has driven a total distance of"+str(distance)+"km" )


class Car(Vehicle):

    def __init__(self, make, total_km, car_type):
        super().__init__(make, total_km)
        self.__car_type = car_type

    def get_car_type(self):
        return self.__car_type

class Motorbike(Vehicle):

    def __init__(self, make, total_km, bike_type):
        super().__init__(make, total_km)
        self.__bike_type = bike_type

    def get_bike_type(self):
        return self.__bike_type

class Manager:
    def __init__(self, name, address, vehicle_rental_system ):
        super().__init__(name, address,)
        self.__vehicle_rental_system = vehicle_rental_system
        print("[manager]"+ super().get_name() + "has to be appointed")

    def add_vehicle(self, vehicle_type):
        print("[Manager] adding the vehicle of type : str(vehicle_type)")

    def remove_vehicle(self, vehicle_type):
        print("[Manager] remove the vehicle of type : " + str(vehicle_type))

    def add_attendant(self, attendant):
        print("[Manager] adding the vehicle attendant [ :" + attendant.get_name())

    def remove_attendant(self, attendant):
            print("[Manager] removing  the vehicle attendant [ :" + attendant.get_name())

class ParkingAttendant(Person):
    def __init__(self, name, address, vehicle_rental_system):
        super().__init__( name, address)
        self.__vehicle_rental_system = vehicle_rental_system

    def inspect_vehicle(self, vehicle):
        print("[parking attendant]: inspected the vehicle")

    def inspect_vehicle(self, vehicle):
        print("[parking attendant]: Accepted the payment by the cash")
        print("[vehicle attendant]: vehicle accepted")


class VehicleRentingSystem:

    def __init__(self, available_vehicle_map, rented_vehicle_map, customer_details_map):
        self.__available_vehicle_map = available_vehicle_map
        self.__rented_vehicle_map = rented_vehicle_map
        self.__customer_details_map = customer_details_map
        print("[VehicleRentingSystem] is initialized")

    def book_vehicle(self, vehicle_type):
        print("[VehicleRentingSystem] vehicle is booked of type" + vehicle_type)

    def accept_back_vehicle(self, vehicle_type):
        print("[VehicleRentingSystem] vehicle is returned of type : "+vehicle_type)

    def customer_payment(self, amount):
        print("[VehicleRentingSystem] accepted from the customer payment of :"+str(amount))


print("############# Booking flow ##########")

vrs = VehicleRentingSystem({},{},{})


address_manager = Address("lane129," "Delhi," "Delhi", 508204, "India")

manager = Manager("Surya", address_manager, vrs)

manager.add_vehicle(CarType.HATCHBACK)
manager.add_vehicle(CarType.LUXURY)
manager.add_vehicle(CarType.SEDAN)
manager.add_vehicle(CarType.SPORTS)
manager.add_vehicle(MotorBikeType.REGULAR)
manager.add_vehicle(MotorBikeType.CRUISER)
manager.add_vehicle(MotorBikeType.DIRT_BIKE)

address_attendant = Address("Paschim vihar," "Delhi," "Delhi", 521175, "India")

attendant = ParkingAttendant("shyam", address_attendant, vrs)

manager.add_attendant(attendant)

address = Address("lane129," "Hyderabad," "telangana", 521175, "India")

customer = Customer("Vishwa", address, "suryatej2608@gmail.com", 9182146802 )

vehicle = Car("Toyota", 3400, CarType.HATCHBACK)

customer.hire_vehicle(CarType.HATCHBACK,vrs)

customer.pick_vehicle(CarType.HATCHBACK, vehicle)

customer.return_vehicle(CarType.HATCHBACK, vrs)

customer.payment(CarType.HATCHBACK, vehicle, attendant)



