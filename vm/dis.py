from instruction import *

OPCODES = {
    0x01: "LITERAL",
    0x11: "ADD",
    0x12: "SUB",
    0x13: "MUL",
    0x14: "DIV",
    0x21: "PRINT",
}

def dis(bytecode):
    """
    >>> dis([LITERAL, 2, PRINT])
    LITERAL 2
    PRINT
    """
    buffer = []
    index = 0
    while index < len(bytecode):
        opcode = bytecode[index]
        if opcode == LITERAL:
            op = OPCODES[opcode]
            x = bytecode[index + 1]
            buffer.append([op, str(x)])
            index += 1
        elif opcode == ADD:
            op = OPCODES[opcode]
            buffer.append([op])
        elif opcode == SUB:
            op = OPCODES[opcode]
            buffer.append([op])
        elif opcode == MUL:
            op = OPCODES[opcode]
            buffer.append([op])
        elif opcode == DIV:
            op = OPCODES[opcode]
            buffer.append([op])
        elif opcode == PRINT:
            op = OPCODES[opcode]
            buffer.append([op])
        index += 1
    
    string = "\n".join([" ".join(x) for x in buffer])
    print(string)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
