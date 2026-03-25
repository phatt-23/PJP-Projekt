
from typing import Union


class Expr:
    pass

class Grp(Expr):
    expr: Expr

class AriNeg(Expr):
    expr: Expr

class Lit(Expr):
    val: Union[int,float,str,bool]


