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

        # support get rid of white space, single-line comments and multiline comments
        # since some of the characters are defined in the lexer, I have to ignore them in order to achieve multi-line comments
        lg.ignore(r"(\s+)|(\/\/.*\n)|(\/\*(.*)|(\s*)\*\/)")
        lg.add("NEWLINE", r"\n") # no longer needed. Newline character is not allowed in mini-js

        # this is solely for debug purpose.
        # white space will not be allowed in the actual interpretation of the program
        lg.add("WHITESPACE", r"\s")

        lg.add("BOOLEANOR", r"\|\|")
        lg.add("BOOLEANAND", r"\&\&")
        
        lg.add("GREATER", r"\>")
        lg.add("LESS", r"\<")
        lg.add("EQUAL_EQUAL", r"\=\=")
        lg.add("NOT_EQUAL", r"\!\=")
        lg.add("GREATER_EQUAL", r"\>\=")
        lg.add("LESS_EQUAL", r"\<\=")
        
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
        lg.add("BOOLEAN", r"true|false")

        lg.add("IDENTIFIER", r"[a-zA-Z_][a-zA-Z0-9_]*")

        self.lexer = lg.build()

    # parse raw program string to token stream
    def lex(self, rawProgramString):
        return self.lexer.lex(rawProgramString)
