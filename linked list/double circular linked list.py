class Node:
    def __init__(self, dataval=None):
        self.data = dataval
        self.next = None
        self.prev = None


class DLinkedList:
    def __init__(self):
        self.headval = None

    # This method is traversing through the list and pritning all the element available in the Linked list
    # Implementation of this method is similar to singly linked list.
    def listprint(self):
        printval = self.headval
        print("Elements in the linked list are: ")
        while printval is not None:
            print(printval.data, end=" <==> ")
            printval = printval.next
        print("None")

    # This method will perform insertion operation before a specific data given by the user.

    def insert_before_data(self, search_data, data):
        current = self.headval
        # if the list is empty return
        if current is None:
            return 0
        # Boundary case
        # if the first element itself matches with the given data
        if self.headval.data == search_data:
            # create the node
            new_node = Node(data)
            # rearrange the nodes
            new_node.next = current
            current.prev = new_node
            self.headval = new_node
            return 1
        else:
            # main case
            # Perform the search operation to find the data user is looking for
            while current is not None and current.data != search_data:
                current = current.next
            # if data not found return 0
            if current is None:
                return 0

            # if data found
            # create the node
            # rearrange the links to make sure that once node is inserted the order is not changed
            # and everything remains same in the linked list
            elif current.data == search_data:
                new_node = Node(data)
                new_node.prev = current.prev
                new_node.next = current
                current.prev.next = new_node
                current.prev = new_node
                return 1
            else:
                return 0

    # This method will find the inserted data in the linked list.
    # This method is also similar to the find method of linked list
    def find_data(self, search_data):
        current = self.headval
        if current is None:
            return 0
        # Logic to find the element
        # this loop will either find the element or it will reach to the end of the list
        while current is not None and current.data != search_data:
            current = current.next
        # checking if the current is reached to the end of the list, if yes return 0
        if current is None:
            return 0
        # if the data is found return 1 to notify the main program
        elif current.data == search_data:
            return 1


if __name__ == "__main__":
    List = DLinkedList()
    first_data = input("Enter the first data of the Linked List: ")
    List.headval = Node(first_data)
    current_node = List.headval
    # while loop to run continously and ask to the user for various listed operations
    while 1:
        # 1 insert data in the list at the end
        # 2. print the content of the list
        # 3. search operation
        # 4. Insert before a specific data (Perform search and then insert)
        # 5. exit the program
        print("1. Enter 1 to insert in list.")
        print("2. Enter 2 to print the list.")
        print("3. Enter 3 to find data in the list.")
        print("4. Enter 4 to insert before specific node.")
        print("0. Enter 0 to exit.")
        choice = int(input("Enter your choice: "))
        # insert operation in the linked list
        if choice == 1:
            data = input("Enter the data you want in the list: ")
            new_node = Node(data)
            new_node.prev = current_node
            current_node.next = new_node
            current_node = new_node
        # printing the content of list
        elif choice == 2:
            List.listprint()

        # searching the data provided by user
        elif choice == 3:
            data = input("Enter the data you want to find: ")
            if (List.find_data(data)):
                print(data, "is available in the linked list.")
            else:
                print(data, "is not avilable in the linked list.")
        # performing insert operation before spcific data
        elif choice == 4:
            # enter the data you are looking for
            search_data = input("Before which element you want to insert: ")
            # enter the data you want to insert
            data = input("Enter the data you want in the list: ")
            # Calling the method
            flag = List.insert_before_data(search_data, data)
            if flag == 1:
                print("Element Inserted.")
            else:
                print("Element not inserted.")
        elif choice == 0:
            break
