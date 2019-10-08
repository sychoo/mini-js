# Simon Chu
# 2019-10-06 21:38:06 Sun EDT
# Program to define the parser

from rply import ParserGenerator
import ast


class Parser:
    def __init__(self):
        # define the parser
        pg = ParserGenerator(
            ["NUMBER", "PLUS", "MINUS", "MULTIPLY", "DIVIDE", "SEMICOLON",
             "PRINT", "PRINTLN", "STRING", "EQUAL", "IDENTIFIER"
             ],
            # A list of precedence rules with ascending precedence, to
            # disambiguate ambiguous production rules.
            precedence=[
                ('left', ['PLUS', 'MINUS']),
                ('left', ['MUL', 'DIV']),
                ('left', ['EQUAL'])
            ])

        # parser definition

        # top-level statements
        @pg.production("main : statements")
        def main(s):
            # return the statement block
            return s[0]

        # multiple statement statements
        @pg.production("statements : statements statement")
        def statements(s):
            return ast.Block(s[0].getASTList() + [s[1]])

        # single statement statements
        @pg.production("statements : statement")
        def statements_statement(s):
            return ast.Block([s[0]])

        # single expression statement
        @pg.production("statement : expr SEMICOLON")
        def statement_expr(s):
            return ast.Statement(s[0])

        # print/println statements
        @pg.production("statement : PRINT expr SEMICOLON")
        @pg.production("statement : PRINTLN expr SEMICOLON")
        def statement_print(s):
            return ast.PrintStatement(s[0].getstr(), s[1])

        # assignment expression
        @pg.production("expr : expr EQUAL expr")
        def expr_assignment(s):
            return ast.AssignmentExpression(s[0], s[2])

        # binary operator expressions
        @pg.production("expr : expr PLUS expr")
        @pg.production("expr : expr MINUS expr")
        @pg.production("expr : expr MULTIPLY expr")
        @pg.production("expr : expr DIVIDE expr")
        def expr_binop(s):
            return ast.BinaryOperator(s[1].getstr(), s[0], s[2])

        # single value/identifier expression
        @pg.production("expr : val")
        def expr_val(s):
            return ast.Expr(s[0])

        # single identifier expression
        @pg.production("expr : IDENTIFIER")
        def expr_id(s):
            return ast.Expr(ast.Identifier(s[0].getstr()))

        # number value
        @pg.production("val : NUMBER")
        def val_number(s):
            return ast.Number(float(s[0].getstr()))

        # string value
        @pg.production("val : STRING")
        def val_string(s):
            return ast.String(s[0].getstr())

        # build the parser
        self.parser = pg.build()

    def parse(self, tokenStream):
        return self.parser.parse(tokenStream)
