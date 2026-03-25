from typing import Optional
from expr import Expr
from dataclasses import dataclass


class Stmt:
    pass

@dataclass
class ExprStmt(Stmt):
    expr: Expr

@dataclass
class Decl(Stmt):
    type: str
    ids: list[str]

@dataclass
class Read(Stmt):
    ids: list[str]

@dataclass
class Write(Stmt):
    exprs: list[Expr]

@dataclass
class Block(Stmt):
    stmts: list[Stmt]

@dataclass
class Cond(Stmt):
    expr: Expr
    then: Stmt
    otherwise: Optional[Stmt]

@dataclass
class Cycle(Stmt):
    expr: Expr
    body: Stmt


