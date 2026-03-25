from typing import Optional
from dataclasses import dataclass
import expr

class Stmt:
    pass

@dataclass
class ExprStmt(Stmt):
    expr: expr.Expr

@dataclass
class Decl(Stmt):
    type: expr.Type
    ids: list[str]

@dataclass
class Read(Stmt):
    ids: list[str]

@dataclass
class Write(Stmt):
    exprs: list[expr.Expr]

@dataclass
class Block(Stmt):
    stmts: list[Stmt]

@dataclass
class Cond(Stmt):
    expr: expr.Expr
    then: Stmt
    otherwise: Optional[Stmt]

@dataclass
class Cycle(Stmt):
    expr: expr.Expr
    body: Stmt


