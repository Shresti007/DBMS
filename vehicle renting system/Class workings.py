#create class company
#Attributes defined outside object can be called with out creating object
class Company:
    name = "XYZ Bank"
    turnover = 5000
    revenue = 1000
    no_of_employees = 100

    def productivity(self):
        return Company.revenue/Company.no_of_employees


#print(getattr("Company.name"))
print(Company.name)
print(Company.turnover)
print(Company.revenue)
print(Company.no_of_employees)
print(Company().productivity())



#Let's take another example. Here, the program below returns output based on the method defined in class
class Company:
    def __init__(self,compname, revenue, employeesize):
        self.name = compname
        self.revenue = revenue
        self.empsiz = employeesize

    def productivity(self):
        return self.revenue/self.empsiz

print(Company("Arya pvt", 100000, 100 ).productivity())

# variables/Attributes of class

class MyCompany:
    # Class Variable
    growth = 0.1

    def __init__(self, compname, revenue, employeesize):
        # Instance Variables
        self.name = compname
        self.revenue = revenue
        self.no_of_employees = employeesize

print(MyCompany.growth) #when

