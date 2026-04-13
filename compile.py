#!/bin/env python3

import sys
from pprint import pprint

import antlr4
from antlr.PJPLexer import PJPLexer
from antlr.PJPParser import PJPParser

from trans import Transformer
from check import Checker
from gen import Generator

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
print(input_text)
print()

lexer = PJPLexer(antlr4.InputStream(input_text))
tok_stream = antlr4.CommonTokenStream(lexer)
parser = PJPParser(tok_stream)

tree = parser.prog()

print("PARSED INPUT:")
print(tree.toStringTree(recog=parser))
print()

trans = Transformer(tok_stream)  

ast = trans.visit(tree)

print("AST:")
pprint(ast)
print()

checker = Checker()
errors = checker.type_check(ast)

print("TYPE CHECK:")
print("\n".join(errors))
print()

if len(errors) != 0:
    sys.exit()

gen = Generator()
out = gen.gen(ast)

print("GENERATED:")
print(out)
print()

if using_file:
    file = sys.argv[1]
    start = max(file.rfind('/'), 0)
    end = file.rfind('.')
    if not out_file:
        out_file = GEN_DIR + file[start:end] + ".stack"
    with open(out_file, 'w+') as f:
        f.write(out)

