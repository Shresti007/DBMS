# SINGLE LINKED LIST
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next  # fine since next is being  used as a function local variable

    def __str__(self):
        return f"{id(self)}:{repr(self.data)} Next: {None if self.next is None else id(self.next)}"


class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def __repr__(self):
        return f"{self.name}"

    def __lt__(self, other):
        return self.name < other.name


class SortedSLL:
    def __init__(self):
        self.head = None

    def add(self, new_data):
        if self.head is None:
            self.head = Node(new_data, None)
            return

        # find location of insertion
        p = None
        n = self.head
        while n is not None and n.data < new_data:
            p = n
            n = n.next

        # insert the node
        if p is None:  # insert in beginning
            temp = Node(new_data, self.head)
            self.head = temp
        else:  # insert  in middle or end
            temp = Node(new_data, n)
            p.next = temp

    def search(self, name):


    def print(self):
        temp = self.head

        if temp is None:
            print("Empty list")
        while temp is not None:
            print(temp)
            temp = temp.next


s = SortedSLL()
s.add(Contact("B", 10))
s.print()

print()
s.add(Contact("A", 10))
s.print()

print()
s.add(Contact("D", 10))
s.print()

print()
s.add(Contact("C", 10))
s.print()
