import sys
from pprint import pprint

import antlr4
from antlr.PJPLexer import PJPLexer
from antlr.PJPParser import PJPParser

from transformer import Transformer

input_text = ""

# get the input text from a file or stdin
if len(sys.argv) >= 2:
    file = sys.argv[1]
    with open(file) as f:
        input_text = f.read()
else:
    input_text = "".join(sys.stdin.readlines())

print("INPUT:")
print(input_text)

lexer = PJPLexer(antlr4.InputStream(input_text))
stream = antlr4.CommonTokenStream(lexer)
parser = PJPParser(stream)

tree = parser.prog()

print("PARSED INPUT:")
print(tree.toStringTree(recog=parser))

transformer = Transformer()  

ast = transformer.visit(tree)

print("AST:")
pprint(ast)

