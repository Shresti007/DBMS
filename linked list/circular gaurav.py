class Node:
    def __init__(self, data=None):
        self.data = data;
        self.next = None;


class CLinkedList:
    def __init__(self):
        self.head = None

    def insert_data(self, data):
        new_node = Node(data)             # creating new node for data insertion
        temp = self.head                  # assigning head to the temp variable
        new_node.next = self.head         # Inserting the node at the beginning of the linked list
        if self.head is not None:        # checkig condition is this is not the first node
            # Running the loop to find the last node in the linked list
            # last node will point to the first node i.e. head node
            while (temp.next != self.head):
                temp = temp.next             # moving to the next node
                                             # After finding the desired node changing the connection
                                             # now it will start poitinting to new node
            temp.next = new_node
        else:
            new_node.next = new_node
        self.head = new_node         # updating the head node so that it will start pointing to the newly created node

    def display(self):
        # print the content of the list
        # Initializing the temp variable for traversal
        temp = self.head
        # checking the condition if there are some elements are there in the linked list
        if self.head is not None:
            # running the loop till temp is traversed once completely
            # after one interation it will point to head node
            # that will be the termination condition to come out of the loop
            while (True):
                # printing the data
                print(temp.data, end=" --> ")
                # moving to the next node
                temp = temp.next
                # comparing of the iteration is done to come out of the loop
                if (temp == self.head):
                    break
            print("head")


if __name__ == "__main__":
    List = CLinkedList()
    # while loop to run continously and ask to the user for various listed operations
    while 1:
        # 1. insert data in the list
        # 2. print the content of the list
        # 3. exit the program
        print("1. Enter 1 to insert in list.")
        print("2. Enter 2 to print the list.")
        print("0. Enter 0 to exit.")
        choice = int(input("Enter your choice: "))
        # insert operation in the linked list
        if choice == 1:
            data = input("Enter the data you want in the list: ")
            List.insert_data(data)
        # printing the content of list
        elif choice == 2:
            print("The data is : ")
            List.display()
            # Exit the program
        elif choice == 0:
            break