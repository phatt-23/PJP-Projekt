from typing import override
import antlr4
from antlr.PJPLexer import PJPLexer
from antlr.PJPListener import PJPListener
from antlr.PJPParser import PJPParser
import sys 

input_text = ""

# get the input text from a file or stdin
if len(sys.argv) >= 2:
    file = sys.argv[1]
    with open(file) as f:
        input_text = f.read()
else:
    input_text = "".join(sys.stdin.readlines())

lexer = PJPLexer(antlr4.InputStream(input_text))
stream = antlr4.CommonTokenStream(lexer)
parser = PJPParser(stream)

tree = parser.prog()
print(tree.toStringTree(recog=parser))

#
# class Stmt():

class Transformer(PJPListener):
    @override
    def enterDecl(self, ctx: PJPParser.DeclContext):
        print('enter decl')

listener = Transformer()  

walker = antlr4.ParseTreeWalker()
walker.walk(listener, tree)

