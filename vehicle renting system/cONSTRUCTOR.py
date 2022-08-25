#COnstructor workings
class Person:
    def __init__(self, Firstname, Lastname):
        self.first = Firstname
        self.last = Lastname

Surya = Person("surya", "karlapati")
print(Surya.last)
