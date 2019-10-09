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
             "PRINT", "PRINTLN", "STRING", "EQUAL", "IDENTIFIER", "BOOLEAN",
             "LBRACE", "RBRACE", "LPAREN", "RPAREN", "IF", "ELSE"
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

        # single if expression, body of if expression can be either statements or expression
        # if expression is evaluated to Null if the body are statements
        # body must be consistent, which means all the clause has to be either expressions or statements
        # don't forget semicolor at the end of the if block
        @pg.production("expr : IF LPAREN expr RPAREN LBRACE expr RBRACE ")
        @pg.production("expr : IF LPAREN expr RPAREN LBRACE statements RBRACE")
        def expr_if(s):
            return ast.IfExpression(s[2], s[5])

        # if - else if - else expression. Else - if is optional
        @pg.production("expr : IF LPAREN expr RPAREN LBRACE expr RBRACE else-if-body-list else-body")
        @pg.production("expr : IF LPAREN expr RPAREN LBRACE statements RBRACE else-if-body-list else-body")
        def expr_if_elseif_else(s):
          return ast.IfElseIfElseExpression(s[2], s[5], s[7], s[8])

        # if - else expression. DO NOT INCLUDE else if body lists (put placeholder empty else if body list)
        @pg.production("expr : IF LPAREN expr RPAREN LBRACE expr RBRACE else-body")
        @pg.production("expr : IF LPAREN expr RPAREN LBRACE statements RBRACE else-body")
        def expr_if_else(s):
          return ast.IfElseIfElseExpression(s[2], s[5], ast.ElseIfBodyList([]), s[7])


        # define the else if body in the case of multiple (one or more) else - if expressions
        @pg.production("else-if-body-list : else-if-body-list else-if-body")
        @pg.production("else-if-body-list : else-if-body-list else-if-body")
        def expr_else_if_body_list(s):
          return ast.ElseIfBodyList(s[0].getASTList() + [s[1]])

        # define a single else-if-body as a else-if-body-list
        @pg.production("else-if-body-list : else-if-body")
        def expr_else_if_body_list__else_if_body(s):
          return ast.ElseIfBodyList([s[0]])

        @pg.production("else-if-body : ELSE IF LPAREN expr RPAREN LBRACE expr RBRACE")
        @pg.production("else-if-body : ELSE IF LPAREN expr RPAREN LBRACE statements RBRACE")
        def expr_else_if_body(s):
          return ast.ElseIfBody(s[3], s[6])

        # define the else body
        @pg.production("else-body : ELSE LBRACE expr RBRACE")
        @pg.production("else-body : ELSE LBRACE statements RBRACE")
        def expr_else_body(s):
          return ast.ElseBody(s[2])

        # number value
        @pg.production("val : NUMBER")
        def val_number(s):
            return ast.Number(float(s[0].getstr()))

        # string value
        @pg.production("val : STRING")
        def val_string(s):
            return ast.String(s[0].getstr())

        # boolean value
        @pg.production("val : BOOLEAN")
        def val_boolean(s):
            return ast.Boolean(s[0].getstr())

        # build the parser
        self.parser = pg.build()

    # return the parsedAST
    def parse(self, tokenStream):
        return self.parser.parse(tokenStream)
