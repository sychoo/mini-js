# define the AST (abstract syntax tree) that the parser will parse to
# all other ASTs inherits from Node
# interpret() function must return the interpreted elements

# main difference between expression and statements: interpret() function for
# expressions returns, interpret() function for statement do not have to return.
import sys

# assignment error


class AssignmentError(Exception):
    pass


# unable to look up identifier value in the context
class ContextError(Exception):
    pass


class NullPointerException(Exception):
    pass


class ConditionError(Exception):
    pass


class TypeError(Exception):
    pass


class Context(object):
    def __init__(self):
        self.context = {}

    def add(self, identifier, value):
        self.context.update({identifier.getValue(): value})

    def lookup(self, identifier):
        try:
            return self.context[identifier.getValue()]
        except KeyError:
            raise ContextError(
                "Identifier specified is not in the scope of the context!")

    def getEmptyContext(self):
        self.context = {}
        return self

    def getContext(self):
        return self.context


class Node(object):
        # equal operator overload
    def __eq__(self, other):
        if not isinstance(other, Node):
            return NotImplemented
            # __dict__ contains object's symbol table
        return (type(self) is type(other) and self.__dict__ == other.__dict__)

    def isSubTypeOf(self, other):
        return type(self) is type(other)
    # not equal to operator overload

    def __ne__(self, other):
        return not (self == other)

    def type(self):
        return type(self)

# define Null type


class Null(Node):
    def __init__(self):
        pass

    def getString(self):
        return "null"

    def getValue(self):
        return None

    def interpret(self, ctx):
        return NullPointerException("Null Cannot Be Interpreted!")

# expression


class Expr(Node):
    def __init__(self, value):
        self.value = value

    def interpret(self, ctx):
        return self.value.interpret(ctx)


# number primitive, all numbers are floats
class Number(Node):
    def __init__(self, value):
        self.value = value

    def add(self, other):
        return Number(self.getValue() + other.getValue())

    def minus(self, other):
        return Number(self.getValue() - other.getValue())

    def multiply():
        return Number(self.getValue() * other.getValue())

    def divide():
        return Number(self.getValue() / other.getValue())

    def getValue(self):
        return self.value

    def getString(self):
        return str(self.getValue())

    def interpret(self, ctx):
        return self


# string primitive
class String(Node):
    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value[1:-1]

    def getString(self):
        return self.getValue()

    def interpret(self, ctx):
        return self


# boolean primitive
class Boolean(Node):
    def __init__(self, value):
        # the value of Boolean will just be python boolean
        if (value == "true"):
            self.value = True
        if (value == "false"):
            self.value = False

    def getValue(self):
        return self.value

    def getString(self):
        if (self.isTrue()):
            return "true"
        elif (self.isFalse()):
            return "false"
        else:
            return TypeError("Boolean value must be either true or false!")

    def isTrue(self):
        return self.value == True

    def isFalse(self):
        return self.value == False

    def interpret(self, ctx):
        return self


# identifier primitive
class Identifier(Node):
    def __init__(self, name):
        self.name = name

    def getValue(self):
        return self.name

    def getString(self):
        return self.getValue()

    def interpret(self, ctx):
        return self


# Block is a list of statement
class Block(Node):
    def __init__(self, statements):
        self.statements = statements

    def getASTList(self):
        return self.statements

    def interpret(self, ctx):
        for statement in self.statements:
            statement.interpret(ctx)


# statement consists of an expression or a chain of expressions to be evaluated
class Statement(Node):
    def __init__(self, expr):
        self.expr = expr

    def interpret(self, ctx):
        self.expr.interpret(ctx)


# unary operator
class UnaryOperator(Node):
    def __init__(self, identifier):
        self.identifier = identifier

    def interpret(self, ctx):
        return NotImplemented


# binary operator
class BinaryOperator(Node):
    def __init__(self, op, left, right):
        self.op = op
        self.left = left
        self.right = right

    def interpret(self, ctx):
        if self.op == "+":
            return self.left.interpret(ctx).add(self.right.interpret(ctx))
        if self.op == "-":
            return self.left.interpret(ctx).minus(self.right.interpret(ctx))
        if self.op == "*":
            return self.left.interpret(ctx).multiply(self.right.interpret(ctx))
        if self.op == "/":
            return self.left.interpret(ctx).divide(self.right.interpret(ctx))
        else:
            return NotImplemented


class AssignmentExpression(Node):
    def __init__(self, left_expr, right_expr):
        self.identifier = left_expr
        self.expr = right_expr

    def interpret(self, ctx):
        # check if LHS is an identifier, raise error if it is not
        self.identifier = self.identifier.interpret(ctx)
        self.expr = self.expr.interpret(ctx)

        if (self.identifier.type() != Identifier):
            raise AssignmentError(
                "LHS of assignment statement must be an identifier")
        if (self.expr.type() == Identifier):
            self.expr = ctx.lookup(self.expr)

        # append the value of the expression to the lhs identifier
        ctx.add(self.identifier, self.expr)


class IfExpression(Node):
    def __init__(self, condition, if_body):
        # condition is an expression that can be evaluated to Boolean
        self.condition = condition

        # statements
        self.if_body = if_body

    def interpret(self, ctx):
        # interpret condition and if_body
        self.condition = self.condition.interpret(ctx)

        # type check conditional statement (must be Boolean)
        if (self.condition.type() != Boolean):
            raise ConditionError(
                "Conditional statement of if statement must be type Boolean.")

        # case when condition is true, execute if block
        if (self.condition.getValue() == True):

            # case when if body consists of expressions
            if (self.if_body.type == Expr):
                return self.if_body.interpret(ctx)

            # case when if body consists of statements
            if (self.if_body.type() == Block):
                self.if_body.interpret(ctx)
                return Null()

        # case when conditional expression is false, return Null
        if (self.condition.getValue() == False):
            return Null()


class IfElseIfElseExpression(Node):
    def __init__(self, condition, if_body, else_if_body_list, else_body):
        self.condition = condition
        self.if_body = if_body
        self.else_if_body_list = else_if_body_list
        self.else_body = else_body

    def interpret(self, ctx):
        # interpret condition and if_body
        self.condition = self.condition.interpret(ctx)

        # type check conditional statement (must be Boolean)
        if (self.condition.type() != Boolean):
            raise ConditionError(
                "Conditional statement of if statement must be type Boolean.")

        # case when condition is true, execute if block
        if (self.condition.getValue() == True):

            # case when if body consists of expressions
            if (self.if_body.type() == Expr):
                return self.if_body.interpret(ctx)

            # case when if body consists of statements
            if (self.if_body.type() == Block):
                self.if_body.interpret(ctx)
                return Null()

        # case when the conditional expression is false, iteratively check expression
        # body list
        if (self.condition.getValue() == False):
            return self.else_if_body_list.interpret(ctx, self.else_body)


# define a list of else-if body
class ElseIfBodyList(Node):
    def __init__(self, else_if_body_list):
        self.else_if_body_list = else_if_body_list

    def getASTList(self):
        return self.else_if_body_list

    def interpret(self, ctx, else_body):
        for else_if_body in self.else_if_body_list:
            # case when case_if_body is evaluated to True
            # evaluate conditional expression first
            if (else_if_body.interpretCondition(ctx).isTrue()):
                # case when else if body consists of expressions
                if (else_if_body.getValue().type() == Expr):
                    return else_if_body.interpretBody(ctx)

                # case when else if body consists of statements
                if (else_if_body.getValue().type() == Block):
                    else_if_body.interpretBody(ctx)
                    return Null()

            # case when the else_if_body is evaluated to False
            if (else_if_body.interpretCondition(ctx).isFalse()):
                continue

        # case when all previous condition expressions are false, execute else_if body
        return else_body.interpret(ctx)

# define else if body


class ElseIfBody(Node):
    def __init__(self, condition, else_if_body):
        self.condition = condition
        self.else_if_body = else_if_body

    def getValue(self):
        return self.else_if_body

    def interpretCondition(self, ctx):
        return self.condition.interpret(ctx)

    def interpretBody(self, ctx):
                # case when if body consists of expressions
        if (self.else_if_body.type() == Expr):
            return self.else_if_body.interpret(ctx)

        # case when if body consists of statements
        if (self.else_if_body.type() == Block):
            self.else_if_body.interpret(ctx)
            return Null()

# define else body


class ElseBody(Node):
    def __init__(self, else_body):
        # note that else doesn't have conditional expression
        self.else_body = else_body

    def getValue(self):
        return self.else_body

    def interpret(self, ctx):
        # case when if body consists of expressions
        if (self.else_body.type() == Expr):
            return self.else_body.interpret(ctx)

        # case when if body consists of statements
        if (self.else_body.type() == Block):
            self.else_body.interpret(ctx)
            return Null()


class PrintStatement(Node):
    def __init__(self, cmd, expr):
        self.expr = expr
        self.cmd = cmd

    def interpret(self, ctx):
        # evaluate expression
        self.expr = self.expr.interpret(ctx)

        # check whether the expressions are Number and String primitives
        if (self.expr.type() == Number or self.expr.type() == String or self.expr.type() == Null or self.expr.type() == Boolean):
            sys.stdout.write(self.expr.getString())

            # handle println, append "\n" at the end
            if self.cmd == "println":
                sys.stdout.write("\n")

            # flush stdout
            sys.stdout.flush()

        if (self.expr.type() == Identifier):
            # look up the identifier value in the context and print it to stdout
            sys.stdout.write(ctx.lookup(self.expr).interpret(ctx).getString())

            # handle println, append "\n" at the end
            if self.cmd == "println":
                sys.stdout.write("\n")

            # flush stdout
            sys.stdout.flush()
        else:
            return NotImplemented
