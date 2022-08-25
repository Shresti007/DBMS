# Polymorphism means the ability to take various forms. It is an important concept when you deal with child and
# parent class. Polymorphism in python is applied through method overriding and method overloading.


# Method Overriding Method overriding allows us to have a method in the child class with the same name as in the
# parent class but the definition of the child class method is different from parent class method.

class Vehicle:
    def message(self):
        print("Parent class method")


class Cab(Vehicle):
    def message(self):
        print("Child Cab class method")


class Bus(Vehicle):
    def message(self):
        print("Child Bus class method")


x = Vehicle()
x.message()

y = Cab()
y.message()

z = Bus()
z.message()


# Method Overloading It allows you to define a function or method with flexibility so that you can call it with only
# some of the arguments and no need to specify the other arguments. You can also call it with all the arguments. You
# can do it whatever the way you want. In the script below, method can be called with no parameter (ignoring phrase
# parameter). Or it can be called with parameter phrase


class Message:

    def details(self, phrase = None):
        if phrase is not None:
            print("my message-", + phrase)

        else:
            print("welcome to our world")




x = Message
x.details("Life is beautiful")
x.details(self="Phrase")
