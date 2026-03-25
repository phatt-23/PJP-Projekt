from typing import Literal, Union
from dataclasses import dataclass

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
    type: Type
    def __init__(self):
        self.type = None

@dataclass
class Grp(Expr):
    expr: Expr

@dataclass
class Una(Expr):
    op: str
    expr: Expr

@dataclass
class Bin(Expr):
    op: str
    left: Expr
    right: Expr

@dataclass
class Ari(Bin):
    # op %,/,*,-,+
    pass

@dataclass
class Rel(Bin):
    # op <,>
    pass

@dataclass
class Comp(Bin):
    # op ==,!=
    pass

@dataclass
class Concat(Bin):
    # op .
    pass

@dataclass
class Log(Bin):
    # op &&,||
    pass

@dataclass
class Assign(Expr):
    id: str
    expr: Expr

@dataclass
class Lit(Expr):
    val: Union[int,float,str,bool]

@dataclass
class Var(Expr):
    id: str

