# Simon Chu
# 2019-10-06 21:38:06 Sun EDT
# Program to define the parser

from rply import ParserGenerator
import ast


class Parser:
    def __init__(self):
        # define the parser
        pg = ParserGenerator(["NUMBER", "PLUS", "MINUS", "MULTIPLY", "DIVIDE", "SEMICOLON", "PRINT", "PRINTLN", "STRING"])

        # parser definition
        @pg.production("main : statements")
        def main(s):
            # return the statement block
            return s[0]

        @pg.production("statements : statements statement")
        def statements(s):
            return ast.Block(s[0].getASTList() + [s[1]])

        @pg.production("statements : statement")
        def statements_statement(s):
            return ast.Block([s[0]])

        @pg.production("statement : expr SEMICOLON")
        def statement_expr(s):
            return ast.Statement(s[0])

        @pg.production("statement : PRINT expr SEMICOLON")
        @pg.production("statement : PRINTLN expr SEMICOLON")
        def statement_print(s):
            return ast.PrintStatement(s[0].getstr(), s[1])

        @pg.production("expr : expr PLUS expr")
        @pg.production("expr : expr MINUS expr")
        @pg.production("expr : expr MULTIPLY expr")
        @pg.production("expr : expr DIVIDE expr")
        def expr_binop(s):
            return ast.BinOp(s[1].getstr(), s[0], s[2])

        @pg.production("expr : NUMBER")
        def expr_number(s):
            return ast.Number(float(s[0].getstr()))

        @pg.production("expr : STRING")
        def expr_string(s):
          return ast.String(s[0].getstr())

        # build the parser
        self.parser = pg.build()

    def parse(self, tokenStream):
        return self.parser.parse(tokenStream)
