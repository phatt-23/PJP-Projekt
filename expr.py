from typing import Union
from dataclasses import dataclass

class Expr:
    pass

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


