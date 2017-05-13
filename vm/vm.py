import array
from opcodes import *
from expressions import *

class VM(object):
    """
    >>> import array
    >>> b = array.array("B", [LITERAL, 0, PRINT])
    >>> bs = b.tostring()
    >>> VM().evaluate(bs)
    0
    >>> VM().evaluatea([LITERAL, 2, PRINT])
    2
    >>> VM().evaluatea([LITERAL, 1, LITERAL, 2, ADD, PRINT])
    3
    >>> VM().evaluatea([LITERAL, 2, LITERAL, 1, SUB, PRINT])
    1
    >>> VM().evaluatea([LITERAL, 2, LITERAL, 3, MUL, PRINT])
    6
    >>> VM().evaluatea([LITERAL, 6, LITERAL, 2, DIV, PRINT])
    3
    """
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        return self.stack.pop()

    def evaluate(self, bytestring):
        bytecode = map(ord, bytestring)
        self.evaluatea(bytecode)

    def evaluatea(self, bytecode):
        index = 0
        while index < len(bytecode):
            code = bytecode[index]
            if code == LITERAL:
                oprand = bytecode[index + 1]
                self.push(NumberExpression(oprand))
                index += 1
            elif code == ADD:
                b = self.pop()
                a = self.pop()
                oprand = AdditionExpression(a, b).evaluate()
                self.push(NumberExpression(oprand))
            elif code == SUB:
                b = self.pop()
                a = self.pop()
                oprand = SubtractionExpression(a, b).evaluate()
                self.push(NumberExpression(oprand))
            elif code == MUL:
                b = self.pop()
                a = self.pop()
                oprand = MultiplicationExpression(a, b).evaluate()
                self.push(NumberExpression(oprand))
            elif code == DIV:
                b = self.pop()
                a = self.pop()
                oprand = DivisionExpression(a, b).evaluate()
                self.push(NumberExpression(oprand))
            elif code == PRINT:
                a = self.pop()
                print(a.evaluate())
            else:
                raise Exception("code: ", code)
            index += 1

if __name__ == "__main__":
    import doctest
    doctest.testmod()
