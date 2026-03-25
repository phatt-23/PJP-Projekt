from typing import override
from antlr.PJPVisitor import PJPVisitor
from antlr.PJPParser import PJPParser
import expr
import stmt 

class Transformer(PJPVisitor):
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
        return stmt.ExprStmt(expr)

    def visitDecl(self, ctx:PJPParser.DeclContext):
        typ = str(ctx.getChild(0))
        ids = [str(ctx.getChild(i)) for i in range(1, ctx.getChildCount(), 2)]
        return stmt.Decl(typ, ids)

    def visitRead(self, ctx:PJPParser.ReadContext):
        ids = [str(ctx.getChild(i)) for i in range(1, ctx.getChildCount(), 2)]
        return stmt.Read(ids)

    def visitWrite(self, ctx:PJPParser.WriteContext):
        exprs = [self.visit(ctx.getChild(i)) for i in range(1, ctx.getChildCount(), 2)]
        return stmt.Write(exprs)

    def visitBlock(self, ctx:PJPParser.BlockContext):
        stmts = [self.visit(ctx.getChild(i)) for i in range(1, ctx.getChildCount() - 1)]
        return stmt.Block(stmts)

    def visitCond(self, ctx:PJPParser.CondContext):
        expr = self.visit(ctx.getChild(2))
        then = self.visit(ctx.getChild(4))
        otherwise = self.visit(ctx.getChild(6)) if ctx.getChildCount() > 6 else None
        return stmt.Cond(expr, then, otherwise)

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
        return expr.Ari(op, left, right)

    def visitAdd(self, ctx:PJPParser.AddContext):
        op, left, right = self.visit_bin(ctx)
        return expr.Ari(op, left, right)

    def visitSub(self, ctx:PJPParser.SubContext):
        op, left, right = self.visit_bin(ctx)
        return expr.Ari(op, left, right)

    def visitMul(self, ctx:PJPParser.MulContext):
        op, left, right = self.visit_bin(ctx)
        return expr.Ari(op, left, right)

    def visitDiv(self, ctx:PJPParser.DivContext):
        op, left, right = self.visit_bin(ctx)
        return expr.Ari(op, left, right)

    def visitRel(self, ctx:PJPParser.RelContext):
        op, left, right = self.visit_bin(ctx)
        return expr.Rel(op, left, right)

    def visitLogOr(self, ctx:PJPParser.LogOrContext):
        op, left, right = self.visit_bin(ctx)
        return expr.Log(op, left, right)

    def visitLogAnd(self, ctx:PJPParser.LogAndContext):
        op, left, right = self.visit_bin(ctx)
        return expr.Log(op, left, right)

    def visitComp(self, ctx:PJPParser.CompContext):
        op, left, right = self.visit_bin(ctx)
        return expr.Comp(op, left, right)

    def visitConcat(self, ctx:PJPParser.ConcatContext):
        op, left, right = self.visit_bin(ctx)
        return expr.Concat(op, left, right)

    def visitLogNeg(self, ctx:PJPParser.LogNegContext):
        op, ex = self.visit_una(ctx)
        return expr.Una(op, ex)

    def visitAriNeg(self, ctx:PJPParser.AriNegContext):
        op, ex = self.visit_una(ctx)
        return expr.Una(op, ex)

    def visitGrp(self, ctx:PJPParser.GrpContext):
        ex = self.visit(ctx.getChild(1))
        return expr.Grp(ex)

    def visitVar(self, ctx:PJPParser.VarContext):
        id = str(ctx.getChild(0))
        return expr.Var(id)

    def visitInt(self, ctx:PJPParser.IntContext):
        val = int(str(ctx.getChild(0)))
        return expr.Lit(val)

    def visitFloat(self, ctx:PJPParser.FloatContext):
        val = float(str(ctx.getChild(0)))
        return expr.Lit(val)

    def visitBool(self, ctx:PJPParser.BoolContext):
        val = str(ctx.getChild(0)) == 'true'
        return expr.Lit(val)

    def visitStr(self, ctx:PJPParser.StrContext):
        val = str(ctx.getChild(0))
        return expr.Lit(val)

    def visitAssign(self, ctx:PJPParser.AssignContext):
        id = str(ctx.getChild(0))
        ex = self.visit(ctx.getChild(2))
        return expr.Assign(id, ex)

