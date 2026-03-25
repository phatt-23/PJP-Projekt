from os import write
from pprint import pprint
import sys
from typing import Union

from expr import type_of_val

V = Union[int, float, bool, str]

class Evaluator:
    vars: dict[str, V]
    stack: list
    jmp_indices: dict[int, int]  # label n -> which cmds

    def __init__(self):
        self.stack = []
        self.vars = {}
        self.handlers = {
            # have types specified
            'add': self.add, 
            'sub': self.sub, 
            'mul': self.mul, 
            'div': self.div,
            'uminus': self.uminus, 
            'gt': self.gt,
            'lt': self.lt,
            'eq': self.eq,
            # these don't
            'mod': self.mod, 
            'cat': self.cat,
            'and': self.AND,
            'or': self.OR,
            # unary
            'not': self.NOT,
            'itof': self.itof,  # not implemented
            # push T x
            'push': self.push,
            'pop': self.pop,
            # ('load' | 'save') id
            'load': self.load,
            'save': self.save,
            # cmd n
            'label': self.label,
            'jmp': self.jmp,
            'fjmp': self.fjmp,
            'print': self.print,
            # read T
            'read': self.read,
        }

        self.idx = 0

    def eval(self, input: str):
        cmds = [
            line for line in input.splitlines()
            if not line.strip().startswith(';') and line.strip()
        ]

        self.cmds = cmds

        pprint(list(enumerate(cmds)))

        self.jmp_indices = { int(c[len('label'):]) : inst_num 
                                for inst_num,c 
                                in [ (inst_num,c) for inst_num,c in enumerate(cmds) if c.startswith('label') ] }

        print("PRINT INDICES:")
        pprint(self.jmp_indices)

        while self.idx < len(cmds):
            curr_idx = self.idx
            cmd = cmds[curr_idx]
            for token, handler in self.handlers.items():
                if cmd.startswith(token):
                    handler(cmd)
                    break
            # print(f"CMD ({curr_idx}) \t '{cmd}'   \t STACK {self.stack} \t VARS {self.vars}")
            self.idx += 1

    def add(self, cmd):
        b = self.stack.pop()
        a = self.stack.pop()
        self.stack.append(a + b)

    def sub(self, cmd):
        b = self.stack.pop()
        a = self.stack.pop()
        self.stack.append(a - b)

    def mul(self, cmd):
        b = self.stack.pop()
        a = self.stack.pop()
        self.stack.append(a * b)

    def div(self, cmd):
        b = self.stack.pop()
        a = self.stack.pop()
        self.stack.append(a / b)

    def uminus(self, cmd):
        a = self.stack.pop()
        self.stack.append(-a)

    def gt(self, cmd):
        b = self.stack.pop()
        a = self.stack.pop()
        self.stack.append(a > b)

    def lt(self, cmd):
        b = self.stack.pop()
        a = self.stack.pop()
        self.stack.append(a < b)

    def eq(self, cmd):
        a = self.stack.pop()
        b = self.stack.pop()
        self.stack.append(a == b)

    def mod(self, cmd):
        b = self.stack.pop()
        a = self.stack.pop()
        self.stack.append(a % b)

    def cat(self, cmd):
        b = self.stack.pop()
        a = self.stack.pop()
        self.stack.append(a + b)

    def AND(self, cmd):
        b = self.stack.pop()
        a = self.stack.pop()
        self.stack.append(a and b)

    def OR(self, cmd):
        b = self.stack.pop()
        a = self.stack.pop()
        self.stack.append(a or b)

    def NOT(self, cmd):
        a = self.stack.pop()
        self.stack.append(not a)

    def itof(self, cmd):
        a = self.stack.pop()
        self.stack.append(float(a))

    def push(self, cmd: str):
        cmd = cmd[len('push'):]
        typ = cmd[:2].strip()
        val = cmd[2:].strip()
        # print(f'PUSH {typ = } {val = }')

        match typ:
            case 'I':
                val = int(val)
            case 'F':
                val = float(val)
            case 'S':
                val = str(val)
            case 'B':
                val = bool(val)
        self.stack.append(val)

    def pop(self, cmd):
        self.stack.pop()

    def load(self, cmd):
        _, id = cmd.split()
        val = self.vars[id]
        self.stack.append(val)

    def save(self, cmd):
        _, id = cmd.split()
        val = self.stack.pop()
        self.vars[id] = val

    def label(self, cmd):
        pass 

    def jmp(self, cmd):
        _, n = cmd.split()
        self.idx = self.jmp_indices[int(n)]

    def fjmp(self, cmd):
        a = self.stack.pop()
        if a == False:
            _, n = cmd.split()
            new = self.jmp_indices[int(n)]
            self.idx = new 

    def print(self, cmd):
        _, n = cmd.split()
        content = list(reversed([str(self.stack.pop()).strip('\'"') for _ in range(int(n))]))
        print("".join(content))
        # print(content)

    def read(self, cmd):
        _, typ = cmd.split()

        inp_text = ''

        try:
            inp_text = sys.stdin.readline()
            print(f'YOU WROTE {inp_text}')
        except:
            pass

        val = None
        match typ:
            case 'I':
                val = int(inp_text) if inp_text else 0
            case 'F':
                val = float(inp_text) if inp_text else 0.0
            case 'S':
                val = str(inp_text).strip('\n') if inp_text else ""
            case 'B':
                val = inp_text == 'true'

        print(f'YOU WROTE {inp_text}')
        self.stack.append(val)

    

