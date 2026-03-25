from os import write
from pprint import pformat, pprint
from stmt import *
from expr import *

class Generator:
    text: str
    stack: list[Type]
    vars: dict[str, Type]
    label_count: int

    def __init__(self):
        self.text = ''
        self.vars = {}
        self.stack = []
        self.label_count = 0


    # utils

    def stack_add(self, t: Type):
        self.stack.append(t)

    def stack_pop(self, by=1):
        for _ in range(by):
            self.stack.pop()

    def fmt_type(self, t: Type):
        match t:
            case 'int':
                return 'INT'
            case 'float':
                return 'FLOAT'
            case 'string':
                return 'STR'
            case 'bool':
                return 'BOOL'
            case None:
                return 'NONE'

    def top_type(self):
        return self.fmt_type(self.stack[-1])

    def write(self, text=''):
        # self.text += f"(stack: {len(self.stack)}) {text} \n";
        self.text += f"{text}\n";

    # stack commands

    def PUSH(self, t: Type, v):
        self.stack_add(t)
        self.write(f"push {self.fmt_type(t)} {v}")

    def READ(self, t: Type):
        self.write(f'read {self.fmt_type(t)}')
        self.stack_add(t)

    def SAVE(self, id):
        self.write(f'save {id}')
        self.stack_pop()

    def LOAD(self, id):
        self.write(f'load {id}')
        self.stack_add(self.vars[id])

    def PRINT(self, n):
        self.write(f"print {n}")
        self.stack_pop(n)

    def POP(self):
        self.write('pop')
        self.stack_pop()

    # generate stmt and expr

    def gen(self, ast: list[Stmt]):
        for stmt in ast:
            self.gen_stmt(stmt)

        return self.text

    def gen_stmt(self, stmt: Stmt):
        stmt_comment = "\n".join(['; ' + line for line in pformat(stmt).splitlines()])

        self.write()
        self.write(stmt_comment)
        self.write()

        match stmt:
            case ExprStmt():
                self.gen_expr(stmt.expr)

            case Decl():
                for id in stmt.ids:
                    self.vars[id] = stmt.type

                    match stmt.type:
                        case 'int':
                            self.PUSH('int', 0)
                        case 'float':
                            self.PUSH('float', 0.0)
                        case 'string':
                            self.PUSH('string', "")
                        case 'bool':
                            self.PUSH('bool', False)
                    self.SAVE(id)

            case Read():
                for id in stmt.ids:
                    self.READ(self.vars[id])
                    self.SAVE(id)

            case Write():
                for e in stmt.exprs:
                    self.gen_expr(e)
                self.PRINT(len(stmt.exprs))

            case Block():
                for st in stmt.stmts:
                    self.gen_stmt(st)

            case Cond():
                self.gen_expr(stmt.expr)
                self.write(f'fjmp {self.label_count}')
                self.gen_stmt(stmt.then)
                self.write(f'label {self.label_count}')
                self.label_count += 1
                if stmt.otherwise:
                    self.gen_stmt(stmt.otherwise)

            case Cycle():
                start = self.label_count
                out = self.label_count + 1
                self.label_count += 2

                self.write(f'label {start}')
                self.gen_expr(stmt.expr)
                self.write(f'fjmp {out}')
                self.gen_stmt(stmt.body)
                self.write(f'jmp {start}')
                self.write(f'label {out}')

        while len(self.stack) > 0:
            self.POP()

    def gen_expr(self, expr: Expr):

        match expr:
            case Grp():
                self.gen_expr(expr.expr)

            case Una():
                self.gen_expr(expr.expr)
                match expr.op:
                    case '-':
                        self.write(f"uminus {self.top_type()}")
                    case '!':
                        self.write('not')

            case Bin():
                self.gen_expr(expr.left)
                self.gen_expr(expr.right)
                match expr.op:
                    case '+':
                        self.write(f'add {self.top_type()}')
                    case '-':
                        self.write(f'sub {self.top_type()}')
                    case '/':
                        self.write(f'div {self.top_type()}')
                    case '*':
                        self.write(f'mul {self.top_type()}')
                    case '%':
                        self.write(f'mod')
                    case '.':
                        self.write(f'cat')
                    case '<':
                        self.write(f'lt {self.top_type()}')
                    case '>':
                        self.write(f'gt {self.top_type()}')
                    case '==':
                        self.write(f'eq {self.top_type()}')
                    case '!=':
                        self.write(f'eq {self.top_type()}')
                        self.write('not')
                t = self.stack[-1]
                self.stack_pop()
                self.stack_pop()
                self.stack_add(t)

            case Assign():
                self.gen_expr(expr.expr)
                self.SAVE(expr.id)
                self.LOAD(expr.id)

            case Lit():
                self.PUSH(type_of_val(expr.val), expr.val)

            case Var():
                self.LOAD(expr.id)
