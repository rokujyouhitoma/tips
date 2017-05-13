from instruction import *

class VM(object):
    """
    >>> VM().evaluate([LITERAL, 2, PRINT])
    2
    >>> VM().evaluate([LITERAL, 1, LITERAL, 2, ADD, PRINT])
    3
    >>> VM().evaluate([LITERAL, 2, LITERAL, 1, SUB, PRINT])
    1
    >>> VM().evaluate([LITERAL, 2, LITERAL, 3, MUL, PRINT])
    6
    >>> VM().evaluate([LITERAL, 6, LITERAL, 2, DIV, PRINT])
    3
    """
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        return self.stack.pop()

    def evaluate(self, bytecode):
        index = 0
        while index < len(bytecode):
            opcode = bytecode[index]
            if opcode == LITERAL:
                value = bytecode[index + 1]
                self.push(value)
                index += 1
            elif opcode == ADD:
                b = self.pop()
                a = self.pop()
                value = a + b
                self.push(value)
            elif opcode == SUB:
                b = self.pop()
                a = self.pop()
                value = a - b
                self.push(value)
            elif opcode == MUL:
                b = self.pop()
                a = self.pop()
                value = a * b
                self.push(value)
            elif opcode == DIV:
                b = self.pop()
                a = self.pop()
                value = a / b
                self.push(value)
            elif opcode == PRINT:
                a = self.pop()
                print(a)
            else:
                raise Exception("opcode: ", opcode)
            index += 1

if __name__ == "__main__":
    import doctest
    doctest.testmod()
