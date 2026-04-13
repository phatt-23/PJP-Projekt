from typing import Optional
from dataclasses import dataclass
from expr import Expr, Type
from loc import Loc

class Stmt():
    loc: Loc = Loc()
    def __init__(self, loc=None) -> None:
        if loc:
            self.loc = loc

@dataclass
class ExprStmt(Stmt):
    expr: Expr
    def __init__(self, expr, loc=None) -> None:
        super().__init__(loc)
        self.expr = expr

@dataclass
class Decl(Stmt):
    type: Type
    ids: list[str]
    def __init__(self, type, ids, loc=None) -> None:
        super().__init__(loc)
        self.type = type
        self.ids = ids

@dataclass
class Read(Stmt):
    ids: list[str]
    def __init__(self, ids, loc=None) -> None:
        super().__init__(loc)
        self.ids

@dataclass
class Write(Stmt):
    exprs: list[Expr]
    def __init__(self, exprs, loc=None) -> None:
        super().__init__(loc)
        self.exprs = exprs

@dataclass
class Block(Stmt):
    stmts: list[Stmt]
    def __init__(self, stmts, loc=None) -> None:
        super().__init__(loc)
        self.stmts = stmts

@dataclass
class Cond(Stmt):
    expr: Expr
    then: Stmt
    otherwise: Optional[Stmt]
    def __init__(self, expr, then, otherwise, loc=None) -> None:
        super().__init__(loc)
        self.expr, self.then, self.otherwise = expr, then, otherwise

@dataclass
class Cycle(Stmt):
    expr: Expr
    body: Stmt
    def __init__(self, expr, body, loc=None) -> None:
        super().__init__(loc)
        self.expr = epxr
        self.body = body


