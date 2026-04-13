from typing import override

import antlr4
from antlr.PJPVisitor import PJPVisitor
from antlr.PJPParser import PJPParser
import expr
from loc import Loc
import stmt 

class Transformer(PJPVisitor):
    tok_stream: antlr4.CommonTokenStream

    def __init__(self, tok_stream: antlr4.CommonTokenStream) -> None:
        super().__init__()
        self.tok_stream = tok_stream


    def visitProg(self, ctx:PJPParser.ProgContext):
        prog = []

        i = 0
        while i < ctx.getChildCount():
            stmt = self.visit(ctx.getChild(i))
            if stmt:
                prog.append(stmt)
            i += 1

        return prog

    def visitEmpty(self, ctx:PJPParser.EmptyContext):
        return None

    def visitExprStmt(self, ctx:PJPParser.ExprStmtContext):
        expr = self.visit(ctx.getChild(0))
        return stmt.ExprStmt(expr, self.create_loc(ctx))

    def visitDecl(self, ctx:PJPParser.DeclContext):
        typ = str(ctx.getChild(0))
        ids = [str(ctx.getChild(i)) for i in range(1, ctx.getChildCount(), 2)]
        return stmt.Decl(typ, ids, self.create_loc(ctx))

    def visitRead(self, ctx:PJPParser.ReadContext):
        ids = [str(ctx.getChild(i)) for i in range(1, ctx.getChildCount(), 2)]
        return stmt.Read(ids, self.create_loc(ctx))

    def visitWrite(self, ctx:PJPParser.WriteContext):
        exprs = [self.visit(ctx.getChild(i)) for i in range(1, ctx.getChildCount(), 2)]
        return stmt.Write(exprs, self.create_loc(ctx))

    def visitBlock(self, ctx:PJPParser.BlockContext):
        stmts = [self.visit(ctx.getChild(i)) for i in range(1, ctx.getChildCount() - 1)]
        return stmt.Block(stmts, self.create_loc(ctx))

    def visitCond(self, ctx:PJPParser.CondContext):
        expr = self.visit(ctx.getChild(2))
        then = self.visit(ctx.getChild(4))
        otherwise = self.visit(ctx.getChild(6)) if ctx.getChildCount() > 6 else None
        return stmt.Cond(expr, then, otherwise, self.create_loc(ctx))

    def visitCycle(self, ctx:PJPParser.CycleContext):
        expr = self.visit(ctx.getChild(2))
        body = self.visit(ctx.getChild(4))
        return stmt.Cycle(expr, body)

    def visit_bin(self, ctx: PJPParser.ExprContext):
        left = self.visit(ctx.getChild(0))
        op = str(ctx.getChild(1))
        right = self.visit(ctx.getChild(2))
        return op, left, right

    def visit_una(self, ctx: PJPParser.ExprContext):
        op = str(ctx.getChild(0))
        e = self.visit(ctx.getChild(1))
        return op, e

    def visitMod(self, ctx:PJPParser.ModContext):
        op, left, right = self.visit_bin(ctx)
        return expr.Ari(op, left, right, self.create_loc(ctx))

    def visitAdd(self, ctx:PJPParser.AddContext):
        op, left, right = self.visit_bin(ctx)
        return expr.Ari(op, left, right, self.create_loc(ctx))

    def visitSub(self, ctx:PJPParser.SubContext):
        op, left, right = self.visit_bin(ctx)
        return expr.Ari(op, left, right, self.create_loc(ctx))

    def visitMul(self, ctx:PJPParser.MulContext):
        op, left, right = self.visit_bin(ctx)
        return expr.Ari(op, left, right, self.create_loc(ctx))

    def visitDiv(self, ctx:PJPParser.DivContext):
        op, left, right = self.visit_bin(ctx)
        return expr.Ari(op, left, right, self.create_loc(ctx))

    def visitRel(self, ctx:PJPParser.RelContext):
        op, left, right = self.visit_bin(ctx)
        return expr.Rel(op, left, right, self.create_loc(ctx))

    def visitLogOr(self, ctx:PJPParser.LogOrContext):
        op, left, right = self.visit_bin(ctx)
        return expr.Log(op, left, right, self.create_loc(ctx))

    def visitLogAnd(self, ctx:PJPParser.LogAndContext):
        op, left, right = self.visit_bin(ctx)
        return expr.Log(op, left, right, self.create_loc(ctx))

    def visitComp(self, ctx:PJPParser.CompContext):
        op, left, right = self.visit_bin(ctx)
        return expr.Comp(op, left, right, self.create_loc(ctx))

    def visitConcat(self, ctx:PJPParser.ConcatContext):
        op, left, right = self.visit_bin(ctx)
        return expr.Concat(op, left, right, self.create_loc(ctx))

    def visitLogNeg(self, ctx:PJPParser.LogNegContext):
        op, ex = self.visit_una(ctx)
        return expr.Una(op, ex, self.create_loc(ctx))

    def visitAriNeg(self, ctx:PJPParser.AriNegContext):
        op, ex = self.visit_una(ctx)
        return expr.Una(op, ex, self.create_loc(ctx))

    def visitGrp(self, ctx:PJPParser.GrpContext):
        ex = self.visit(ctx.getChild(1))
        return expr.Grp(ex, self.create_loc(ctx))

    def visitVar(self, ctx:PJPParser.VarContext):
        id = str(ctx.getChild(0))
        return expr.Var(id, self.create_loc(ctx))

    def visitInt(self, ctx:PJPParser.IntContext):
        val = int(str(ctx.getChild(0)))
        return self.create_lit(val, ctx)

    def visitFloat(self, ctx:PJPParser.FloatContext):
        val = float(str(ctx.getChild(0)))
        return self.create_lit(val, ctx)

    def visitBool(self, ctx:PJPParser.BoolContext):
        val = str(ctx.getChild(0)) == 'true'
        return self.create_lit(val, ctx)

    def visitStr(self, ctx:PJPParser.StrContext):
        val = str(ctx.getChild(0))
        return self.create_lit(val, ctx)

    def create_lit(self, val, ctx):
        return expr.Lit(val, self.create_loc(ctx))

    def create_loc(self, ctx):
        token_interval: tuple = ctx.getSourceInterval()
        tok: antlr4.Token = self.tok_stream.get(token_interval[0])
        return Loc(tok.line, tok.column)

    def visitAssign(self, ctx:PJPParser.AssignContext):
        id = str(ctx.getChild(0))
        ex = self.visit(ctx.getChild(2))
        return expr.Assign(id, ex, self.create_loc(ctx))

