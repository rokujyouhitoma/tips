import array
from opcodes import *

OPCODES = {
    LITERAL: "LITERAL",
    ADD: "ADD",
    SUB: "SUB",
    MUL: "MUL",
    DIV: "DIV",
    PRINT: "PRINT",
}

def dis(bytestring):
    """
    >>> import array
    >>> ba = array.array("B", [LITERAL, 2, PRINT])
    >>> bs = ba.tostring()
    >>> dis(bs)
    LITERAL 2
    PRINT
    """
    bytecode = map(ord, bytestring)
    disa(bytecode)

def disa(bytecode):
    """
    >>> disa([LITERAL, 2, PRINT])
    LITERAL 2
    PRINT
    """
    buffer = []
    index = 0
    while index < len(bytecode):
        code = bytecode[index]
        if code == LITERAL:
            opcode = OPCODES[code]
            oprand = bytecode[index + 1]
            buffer.append([opcode, str(oprand)])
            index += 1
        elif code == ADD:
            opcode = OPCODES[code]
            buffer.append([opcode])
        elif code == SUB:
            opcode = OPCODES[code]
            buffer.append([opcode])
        elif code == MUL:
            opcode = OPCODES[code]
            buffer.append([opcode])
        elif code == DIV:
            opcode = OPCODES[code]
            buffer.append([opcode])
        elif code == PRINT:
            opcode = OPCODES[code]
            buffer.append([opcode])
        index += 1
    
    string = "\n".join([" ".join(x) for x in buffer])
    print(string)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
