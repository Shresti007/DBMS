class Stack:
    def __init__(self, size):
        self.__buffer = list()
        self.__size = size

    def push(self, data):
        if len(self.__buffer) >= self.__size:
            raise Exception("Overflow")

        self.__buffer.append(data)

    def pop(self):
        if len(self.__buffer) == 0:
            raise Exception("Underflow")

        return self.__buffer.pop()

    def is_empty(self):
        return len(self.__buffer) == 0

    def peek(self):
        if len(self.__buffer) == 0:
            raise Exception("Underflow")

        return self.__buffer[-1]

    def print(self):
        print("Stack:", self.__buffer)


if __name__ == "__main__":
    s = Stack(4)

    try:
        s.push(1)
        s.push(2)
        s.push(3)
        s.push(4)
        s.push(5)
    except Exception as err:
        print("Something went wrong: ", err)
    print()

    try:
        for i in range(4):
            print("pop:", s.pop())
    except Exception as err:
        print("Something went wrong: ", err)

    s.print()
    s.push(1)
    s.print()
