def print_ll(self):
    if self.head is None:
        print("no dll is resent")
    else:
        n = self.head
        while n.next is not None:
            print(n.data , end = "-->")
            n = n.next
        while n is not None:
            print(n.data)
            n = n.prev

    def add_before(self):
        if self.head is None:
            print(LL is empty)
            return
        else:
            n = self.head
            while n is not None:
                if x == n.data
                    break
                n = n.next
            if n in None:
                retunr ("x is not avaialble in dll")
            else:
                new_node = Node(data)
                new_node.next = n
                n.prev = new_node
                if n.prev is not None:
                    n.prev.next = new_node
                else:
                    self.head = new_node



def delete_value(self, x):
    if self.head is None:
        print("DLL is Empty")
    elif self.head.next is not None:
        print("DLL is empty afte deletiing the first node")
    elif self.head.next == x:
        self.head = self.head.next
        self.head.prev = None

    n = self.head
    while n.next is not None:
        if x == n.data:
            break
        n = n.next
    while n.next is not None:
        n.next.prev = n.prev
        n.prev.next = n.next
    else:
        if n.data == x:
            n.prev.next = None
        else:
            print("VAlue with termed x i not found")
