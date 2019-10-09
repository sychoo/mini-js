# Simon Chu
# 2019-10-06 21:38:06 Sun EDT
# Program to define the lexer

from rply import LexerGenerator


class Lexer:
    def __init__(self):
        lg = LexerGenerator()
        # ignore begin and ending white spaces
        #lg.ignore(r"\s+") # original
        #lg.ignore(r"[^\S\n\r\f]+") # this is the regex that just matches a space (emtpy string)
        #lg.ignore(r"[^\S\n]+") # matches just a space
        lg.ignore(r"(\s+)|(\/\/.*\n)")
        lg.add("NEWLINE", r"\n")
        #lg.add("SLASH", r"\/")
        lg.add("IF", r"if")
        lg.add("ELSE", r"else")
        lg.add("PRINTLN", r"println")
        lg.add("PRINT", r"print")
        lg.add("WHITESPACE", r"\s")
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
        lg.add("BOOLEAN", r"true|false")

        lg.add("IDENTIFIER", r"[a-zA-Z_][a-zA-Z0-9_]*")

        self.lexer = lg.build()

    # parse raw program string to token stream
    def lex(self, rawProgramString):
        return self.lexer.lex(rawProgramString)
