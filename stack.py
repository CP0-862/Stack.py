class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    # Push operation
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    # Pop operation
    def pop(self):
        if self.top is None:
            print("Stack is empty")
            return

        print("Popped:", self.top.data)
        self.top = self.top.next

    # Peek operation
    def peek(self):
        if self.top is None:
            print("Stack is empty")
        else:
            print("Top element:", self.top.data)

    # Display operation
    def display(self):
        if self.top is None:
            print("Stack is empty")
            return

        temp = self.top
        print("Stack:")

        while temp:
            print(temp.data, end=" ")
            temp = temp.next

        print()


# Main program
stack = Stack()

stack.push(10)
stack.push(20)
stack.push(30)

stack.display()

stack.peek()

stack.pop()

stack.display()

stack.peek()
