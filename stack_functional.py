def create_stack():
    return []


def push(a: list, x):
    a.append(x)


def pop(a: list):
    if len(a) > 0:
        return a.pop()
    return None


# example of using
def example():
    my_stack = create_stack()
    while True:
        command = input().split(' ')
        if command[0] == 'push':
            x = command[1]
            push(my_stack, x)
        elif command[0] == 'pop':
            print(pop(my_stack))
        elif command[0] == 'stop' or command[0] == 'finish':
            break
        else:
            raise ValueError('Unknown command')


if __name__ == "__main__":
    example()
