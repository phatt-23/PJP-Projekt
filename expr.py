from typing import Literal, Union, override
from dataclasses import dataclass

from loc import Loc

Type = Literal['int', 'float', 'string', 'bool', None]

def type_of_val(v):
    if isinstance(v, bool):
        return 'bool'
    elif isinstance(v, int):
        return 'int'
    elif isinstance(v, float):
        return 'float'
    elif isinstance(v, str):
        return 'string'
    return None


class Expr:
    loc: Loc = Loc()
    type: Type
    def __init__(self, loc=None):
        self.type = None
        if loc:
            self.loc = loc

@dataclass
class Grp(Expr):
    expr: Expr
    def __init__(self, expr, loc=None):
        super().__init__(loc)
        self.expr = expr

@dataclass
class Una(Expr):
    op: str
    expr: Expr
    def __init__(self, op, expr, loc=None):
        super().__init__(loc)
        self.op = op
        self.expr = expr

@dataclass
class Bin(Expr):
    op: str
    left: Expr
    right: Expr
    def __init__(self, op, left, right, loc=None):
        super().__init__(loc)
        self.op = op
        self.left = left
        self.right = right


@dataclass
class Ari(Bin):
    # op %,/,*,-,+
    def __init__(self, op, left, right, loc=None):
        super().__init__(op, left, right, loc)

@dataclass
class Rel(Bin):
    # op <,>
    def __init__(self, op, left, right, loc=None):
        super().__init__(op, left, right, loc)

@dataclass
class Comp(Bin):
    # op ==,!=
    def __init__(self, op, left, right, loc=None):
        super().__init__(op, left, right, loc)

@dataclass
class Concat(Bin):
    # op .
    def __init__(self, op, left, right, loc=None):
        super().__init__(op, left, right, loc)

@dataclass
class Log(Bin):
    # op &&,||
    def __init__(self, op, left, right, loc=None):
        super().__init__(op, left, right, loc)

@dataclass
class Assign(Expr):
    id: str
    expr: Expr
    def __init__(self, id, expr, loc=None):
        super().__init__(loc)
        self.id = id
        self.expr = expr

@dataclass
class Lit(Expr):
    val: Union[int,float,str,bool]

    def __init__(self, val, loc):
        super().__init__(loc)
        self.val = val

@dataclass
class Var(Expr):
    id: str
    def __init__(self, id, loc=None):
        super().__init__(loc)
        self.id = id

@dataclass
class Itof(Expr):
    # conversion from int to float
    expr: Expr
    def __init__(self, expr, loc=None):
        super().__init__(loc)
        self.expr = expr
        self.type = 'float'
