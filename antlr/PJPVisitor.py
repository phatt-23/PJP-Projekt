# Generated from PJP.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .PJPParser import PJPParser
else:
    from PJPParser import PJPParser

# This class defines a complete generic visitor for a parse tree produced by PJPParser.

class PJPVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by PJPParser#prog.
    def visitProg(self, ctx:PJPParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PJPParser#Empty.
    def visitEmpty(self, ctx:PJPParser.EmptyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PJPParser#ExprStmt.
    def visitExprStmt(self, ctx:PJPParser.ExprStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PJPParser#Decl.
    def visitDecl(self, ctx:PJPParser.DeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PJPParser#Read.
    def visitRead(self, ctx:PJPParser.ReadContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PJPParser#Write.
    def visitWrite(self, ctx:PJPParser.WriteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PJPParser#Block.
    def visitBlock(self, ctx:PJPParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PJPParser#Cond.
    def visitCond(self, ctx:PJPParser.CondContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PJPParser#Cycle.
    def visitCycle(self, ctx:PJPParser.CycleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PJPParser#Add.
    def visitAdd(self, ctx:PJPParser.AddContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PJPParser#Sub.
    def visitSub(self, ctx:PJPParser.SubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PJPParser#Mod.
    def visitMod(self, ctx:PJPParser.ModContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PJPParser#Grp.
    def visitGrp(self, ctx:PJPParser.GrpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PJPParser#Mul.
    def visitMul(self, ctx:PJPParser.MulContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PJPParser#LogOr.
    def visitLogOr(self, ctx:PJPParser.LogOrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PJPParser#Var.
    def visitVar(self, ctx:PJPParser.VarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PJPParser#Int.
    def visitInt(self, ctx:PJPParser.IntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PJPParser#Comp.
    def visitComp(self, ctx:PJPParser.CompContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PJPParser#LogAnd.
    def visitLogAnd(self, ctx:PJPParser.LogAndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PJPParser#LogNeg.
    def visitLogNeg(self, ctx:PJPParser.LogNegContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PJPParser#Str.
    def visitStr(self, ctx:PJPParser.StrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PJPParser#Div.
    def visitDiv(self, ctx:PJPParser.DivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PJPParser#Concat.
    def visitConcat(self, ctx:PJPParser.ConcatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PJPParser#Float.
    def visitFloat(self, ctx:PJPParser.FloatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PJPParser#Bool.
    def visitBool(self, ctx:PJPParser.BoolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PJPParser#Rel.
    def visitRel(self, ctx:PJPParser.RelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PJPParser#AriNeg.
    def visitAriNeg(self, ctx:PJPParser.AriNegContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PJPParser#Assign.
    def visitAssign(self, ctx:PJPParser.AssignContext):
        return self.visitChildren(ctx)



del PJPParser