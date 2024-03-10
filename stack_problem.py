'''Write a Python class called Stack that implements a stack data structure. 
The class should have methods for pushing an element onto the stack, 
popping an element off the stack, and checking if the stack is empty.'''

class Stack:
    stack = []
    def __init__(self):
        self.stack = []
    def Pop(self):
        if self.isEmpty() is True:
            print("Stack is Empty")
        else:
            return self.stack.pop()
    def Push(self, element):
        self.stack.append(element)
    def isEmpty(self):
        return len(self.stack) == 0 
    def Print(self):
        for items in self.stack:
            print(items)

my_stack = Stack()
print(my_stack.isEmpty())
my_stack.Push(1)
my_stack.Push(2)
my_stack.Push(3) # Output: 3
print(my_stack.Pop())    # Output: 3
print(my_stack.Pop())    # Output: 2  # Output: 1
print(my_stack.isEmpty())


