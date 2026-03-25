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
        type = str(ctx.getChild(0))
        ids = [str(ctx.getChild(i)) for i in range(1, ctx.getChildCount(), 2)]
        return stmt.Decl(type, ids)

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
        return expr.Bin(op, left, right)

    def visit_una(self, ctx: PJPParser.ExprContext):
        op = str(ctx.getChild(0))
        e = self.visit(ctx.getChild(1))
        return expr.Una(op, e)

    def visitAdd(self, ctx:PJPParser.AddContext):
        return self.visit_bin(ctx) 

    def visitSub(self, ctx:PJPParser.SubContext):
        return self.visit_bin(ctx) 

    def visitMod(self, ctx:PJPParser.ModContext):
        return self.visit_bin(ctx) 

    def visitGrp(self, ctx:PJPParser.GrpContext):
        return self.visit_bin(ctx) 

    def visitMul(self, ctx:PJPParser.MulContext):
        return self.visit_bin(ctx) 

    def visitLogOr(self, ctx:PJPParser.LogOrContext):
        return self.visit_bin(ctx) 

    def visitLogAnd(self, ctx:PJPParser.LogAndContext):
        return self.visit_bin(ctx) 

    def visitVar(self, ctx:PJPParser.VarContext):
        id = str(ctx.getChild(0))
        return expr.Var(id)

    def visitComp(self, ctx:PJPParser.CompContext):
        return self.visit_bin(ctx)

    def visitLogNeg(self, ctx:PJPParser.LogNegContext):
        return self.visit_una(ctx)

    def visitDiv(self, ctx:PJPParser.DivContext):
        return self.visit_bin(ctx)

    def visitConcat(self, ctx:PJPParser.ConcatContext):
        return self.visit_bin(ctx)

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

    def visitRel(self, ctx:PJPParser.RelContext):
        return self.visit_bin(ctx)

    def visitAriNeg(self, ctx:PJPParser.AriNegContext):
        return self.visit_una(ctx)

    def visitAssign(self, ctx:PJPParser.AssignContext):
        id = str(ctx.getChild(0))
        ex = self.visit(ctx.getChild(2))
        return expr.Assign(id, ex)

