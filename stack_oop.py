class Stack:
    def __init__(self):
        self.a = []

    def push(self, x):
        self.a.append(x)

    def pop(self):
        if len(self.a) > 0:
            return self.a.pop()
        raise IndexError('Cannot pop from empty stack')


# example of using
def example():
    my_stack = Stack()
    while True:
        command = input().split(' ')
        if command[0] == 'push':
            x = command[1]
            my_stack.push(x)
        elif command[0] == 'pop':
            print(my_stack.pop())
        elif command[0] == 'stop' or command[0] == 'finish':
            break
        else:
            raise ValueError('Unknown command')


if __name__ == '__main__':
    example()
