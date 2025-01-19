from typing import Any

class Stack(object):
    def __init__(self) -> None:
        self.stack = []

    def push(self, data) -> None:
        self.stack.append(data)
    
    def pop(self) -> Any:
        if self.stack:
            return self.stack.pop()
        

if __name__ == '__main__':
    s = Stack()

    s.push(1)
    s.push(2)
    s.push(3)
    print(s.stack)
    print(s.pop())
    print(s.stack)
    print(s.pop())
    print(s.pop())