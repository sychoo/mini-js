# Simon Chu
# 2019-10-06 21:38:06 Sun EDT
# Program to define the lexer

from rply import LexerGenerator


class Lexer:
    def __init__(self):
        lg = LexerGenerator()
        lg.ignore(r"\s+")
        lg.add("IF", r"if")
        lg.add("ELSE", r"else")
        lg.add("PRINTLN", r"println")
        lg.add("PRINT", r"print")

        lg.add("LPAREN", r"\(")
        lg.add("RPAREN", r"\)")
        lg.add("LBRACE", r"\{")
        lg.add("RBRACE", r"\}")

        lg.add("EQUAL", r"=")
        lg.add("PLUS", r"\+")
        lg.add("MINUS", r"-")
        lg.add("MULTIPLY", r"\*")
        lg.add("DIVIDE", r"/")

        lg.add("GREATER_EQUAL", r">=")
        lg.add("LESS_EQUAL", r"<=")

        lg.add("SEMICOLON", r";")
        lg.add("NUMBER", r"\d+")
        lg.add("STRING", r"\".*\"")
        lg.add("IDENTIFIER", r"[a-zA-Z_][a-zA-Z0-9_]*")

        self.lexer = lg.build()

    # parse raw program string to token stream
    def lex(self, rawProgramString):
        return self.lexer.lex(rawProgramString)
