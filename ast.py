# define the AST (abstract syntax tree) that the parser will parse to
# all other ASTs inherits from Node

import sys


class Node(object):
    # equal operator overload
    def __eq__(self, other):
        if not isinstance(other, Node):
            return NotImplemented
        return (type(self) is type(other) and self.__dict__ == other.__dict__)
    
    def isSubTypeOf(self, other):
      return type(self) is type(other)
    # not equal to operator overload

    def __ne__(self, other):
        return not (self == other)
    
    def type(self):
      return type(self)


class Block(Node):
    def __init__(self, statements):
        self.statements = statements

    def getASTList(self):
        return self.statements

    def interpret(self, ctx):
        for statement in self.statements:
            statement.interpret(ctx)


class Statement(Node):
    def __init__(self, expr):
        self.expr = expr

    def compile(self, ctx):
        self.expr.compile(ctx)
        ctx.emit(POP_TOP)

    def interpret(self, ctx):
        self.expr.interpret(ctx)


class Number(Node):
    def __init__(self, value):
        self.value = value

    def compile(self, ctx):
        ctx.emit(LOAD_CONST, ctx.new_const(JSNumber(self.value)))

    def interpret(self, ctx):
        return self.value


class String(Node):
    def __init__(self, value):
        self.value = value

    def interpret(self, ctx):
        return self.value


class BinOp(Node):
    def __init__(self, op, left, right):
        self.op = op
        self.left = left
        self.right = right

    def compile(self, ctx):
        self.left.compile(ctx)
        self.right.compile(ctx)
        opname = {
            "+": "BINARY_ADD",
        }
        ctx.emit(opname[self.op])

    def interpret(self, ctx):
        if self.op == "+":
            return self.left.interpret(ctx) + self.right.interpret(ctx)
        else:
            return NotImplemented


class Assignment(Node):
    def __init__(self, left, right):
        self.left = left
        self.right = right


class IfStatement(Node):
    def __init__(self, condition, ifBlockStatements):
        self.condition = condition
        self.statements = ifBlockStatements


class IfElseStatement(Node):
    def __init__(self, condition, ifBlockStatements, elseBlockStatements):
        self.condition = condition
        self.ifBlockStatements = ifBlockStatements
        self.elseBlockStatements = elseBlockStatements


class PrintStatement(Node):
    def __init__(self, cmd, expr):
        self.expr = expr
        self.cmd = cmd

    def interpret(self, ctx):
        # print string
        if self.expr.type() == String:
            # strip the quotes around the string
            sys.stdout.write(self.expr.value[1:-1])

            # handle println, append "\n" at the end
            if self.cmd == "println":
                sys.stdout.write("\n")

            # flush stdout
            sys.stdout.flush()

        if (self.expr.type() == Number):
            # write the numeric value
            sys.stdout.write(self.expr.value)

            # handle println, append "\n" at the end
            if self.cmd == "println":
                sys.stdout.write("\n")

            # flush stdout
            sys.stdout.flush()
