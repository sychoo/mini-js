# Simon Chu
# 2019-10-06 21:38:06 Sun EDT
# Program to define the interpreter

# define world's simplest interpreter
class Interpreter(object):
    def __init__(self, bytecode):
        self.bytecode = bytecode

        # program code, indicates where in the byte code are you
        self.pc = 0
        while pc < len(self.bytecode):
            opcode = self.bytecode[pc]
            opname = OPCODE_TO_NAME[opcode]
            pc = getattr(self, opname) (pc)
    def LOAD_CONST(self, pc):
        arg = order(self.bytecode[pc + 1])
        self.push(self.consts[arg])
        return pc + 2
    def BINARY_ADD(self, pc):
        right = self.pop()
        left = self.pop()
        self.push(left.add(right))
        return pc + 1

#stream = lexer.lex("1; 2;")
#print(stream.next())
#print(stream.next())
#print(parser.parse(stream).compile())
#stream2 = lexer.lex("2;")

# compare two node object
#print(parser.parse(stream2) == parser.parse(stream))