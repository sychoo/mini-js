# Simon Chu
# 2019-10-06 21:38:06 Sun EDT
# Interpreter program to run program
# https://www.youtube.com/watch?v=LCslqgM48D4

''' This interpreter interprets the following language (A subset of javascript)
a = 3;
if (a >= 2) {
	print "a is big!";
}
else {
	print a;
}
'''

from lexer import Lexer
from parser import Parser
import ast
import sys


def getRawProgramString(filename):
    lines = open(filename, "r").readlines()
    rawString = "".join(lines)
    return rawString


def main():
    # check command line argument and print usage message
    if len(sys.argv) != 2:
        print("usage: python interp.py <program to execute>")
        exit()

    # create lexer
    lexer = Lexer()
    tokenStream = lexer.lex(getRawProgramString(sys.argv[1]))

    # create parser
    parser = Parser()
    parsedAST = parser.parse(tokenStream)

    # interpret the block
    print("\n>>> Executing >>>")
    parsedAST.interpret(ast.Context().getEmptyContext())
    print("<<< Terminated <<<\n")


if __name__ == "__main__":
    main()
