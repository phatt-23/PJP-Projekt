#!/bin/env python3

import sys
from pprint import pprint

import antlr4
from antlr.PJPLexer import PJPLexer
from antlr.PJPParser import PJPParser
from antlr4.error.ErrorListener import ErrorListener

from trans import Transformer
from check import Checker
from gen import Generator


class MyErrListener(ErrorListener):
    def __init__(self):
        super().__init__()
        self.has_error = False
        self.errs = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.has_error = True
        recognizer_name = "lexer" if type(recognizer) == PJPLexer else "parser"
        self.errs.append(f"[{line}:{column}] {recognizer_name} error - {msg}")


GEN_DIR = "./gen/"

input_text = ""
using_file = len(sys.argv) >= 2

out_file = sys.argv[2] if len(sys.argv) >= 3 else None


# get the input text from a file or stdin

if using_file:
    file = sys.argv[1]
    with open(file) as f:
        input_text = f.read()
else:
    input_text = "".join(sys.stdin.readlines())

print("INPUT:")
print(input_text, end="\n\n", flush=True)


# parse the read input

err_listener = MyErrListener()

print("ANTLR Lexing...")
lexer = PJPLexer(antlr4.InputStream(input_text))
lexer.removeErrorListeners()
lexer.addErrorListener(err_listener)

tok_stream = antlr4.CommonTokenStream(lexer)  # runs lexer

print("ANTLR Parsing...")
parser = PJPParser(tok_stream)
parser.removeErrorListeners()
parser.addErrorListener(err_listener)

tree = parser.prog()  # runs parser

print("PARSED INPUT:")
print(tree.toStringTree(recog=parser), end="\n\n", flush=True)


if err_listener.has_error:
    print("\n".join(err_listener.errs))
    print("Parsing error occured. Exiting!")
    sys.exit(0)


# transform the antlr tree into my repr

trans = Transformer(tok_stream)  

ast = trans.visit(tree)

print("AST:")
pprint(ast)
print(flush=True)


# type check

checker = Checker(ast)
errors = checker.type_check()

print("TYPE CHECK:")

if len(errors) != 0:
    print("\n".join(errors), end="\n\n", flush=True)
    sys.exit()
else:
    print("All OK", end="\n\n")

if checker.changed_prog:
    print("AST CHANGED:")
    pprint(ast)
    print(flush=True)


# generate the stack code

gen = Generator()
out = gen.gen(ast)

print("GENERATED:")
print(out, end="\n\n", flush=True)

if using_file:
    file = sys.argv[1]
    start = max(file.rfind('/'), 0)
    end = file.rfind('.')
    if not out_file:
        out_file = GEN_DIR + file[start:end] + ".stack"
    with open(out_file, 'w+') as f:
        f.write(out)

