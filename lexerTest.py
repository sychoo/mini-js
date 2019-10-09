# Simon Chu
# 2019-10-08 15:03:07 EDT Tuesday

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

    # lexer debug clause
    for token in tokenStream:
        print(token)


if __name__ == "__main__":
    main()
