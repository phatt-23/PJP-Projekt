# Generated from PJP.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .PJPParser import PJPParser
else:
    from PJPParser import PJPParser

# This class defines a complete listener for a parse tree produced by PJPParser.
class PJPListener(ParseTreeListener):

    # Enter a parse tree produced by PJPParser#prog.
    def enterProg(self, ctx:PJPParser.ProgContext):
        pass

    # Exit a parse tree produced by PJPParser#prog.
    def exitProg(self, ctx:PJPParser.ProgContext):
        pass


    # Enter a parse tree produced by PJPParser#Empty.
    def enterEmpty(self, ctx:PJPParser.EmptyContext):
        pass

    # Exit a parse tree produced by PJPParser#Empty.
    def exitEmpty(self, ctx:PJPParser.EmptyContext):
        pass


    # Enter a parse tree produced by PJPParser#ExprStmt.
    def enterExprStmt(self, ctx:PJPParser.ExprStmtContext):
        pass

    # Exit a parse tree produced by PJPParser#ExprStmt.
    def exitExprStmt(self, ctx:PJPParser.ExprStmtContext):
        pass


    # Enter a parse tree produced by PJPParser#Decl.
    def enterDecl(self, ctx:PJPParser.DeclContext):
        pass

    # Exit a parse tree produced by PJPParser#Decl.
    def exitDecl(self, ctx:PJPParser.DeclContext):
        pass


    # Enter a parse tree produced by PJPParser#Read.
    def enterRead(self, ctx:PJPParser.ReadContext):
        pass

    # Exit a parse tree produced by PJPParser#Read.
    def exitRead(self, ctx:PJPParser.ReadContext):
        pass


    # Enter a parse tree produced by PJPParser#Write.
    def enterWrite(self, ctx:PJPParser.WriteContext):
        pass

    # Exit a parse tree produced by PJPParser#Write.
    def exitWrite(self, ctx:PJPParser.WriteContext):
        pass


    # Enter a parse tree produced by PJPParser#Block.
    def enterBlock(self, ctx:PJPParser.BlockContext):
        pass

    # Exit a parse tree produced by PJPParser#Block.
    def exitBlock(self, ctx:PJPParser.BlockContext):
        pass


    # Enter a parse tree produced by PJPParser#Cond.
    def enterCond(self, ctx:PJPParser.CondContext):
        pass

    # Exit a parse tree produced by PJPParser#Cond.
    def exitCond(self, ctx:PJPParser.CondContext):
        pass


    # Enter a parse tree produced by PJPParser#Cycle.
    def enterCycle(self, ctx:PJPParser.CycleContext):
        pass

    # Exit a parse tree produced by PJPParser#Cycle.
    def exitCycle(self, ctx:PJPParser.CycleContext):
        pass


    # Enter a parse tree produced by PJPParser#Add.
    def enterAdd(self, ctx:PJPParser.AddContext):
        pass

    # Exit a parse tree produced by PJPParser#Add.
    def exitAdd(self, ctx:PJPParser.AddContext):
        pass


    # Enter a parse tree produced by PJPParser#Sub.
    def enterSub(self, ctx:PJPParser.SubContext):
        pass

    # Exit a parse tree produced by PJPParser#Sub.
    def exitSub(self, ctx:PJPParser.SubContext):
        pass


    # Enter a parse tree produced by PJPParser#Mod.
    def enterMod(self, ctx:PJPParser.ModContext):
        pass

    # Exit a parse tree produced by PJPParser#Mod.
    def exitMod(self, ctx:PJPParser.ModContext):
        pass


    # Enter a parse tree produced by PJPParser#Grp.
    def enterGrp(self, ctx:PJPParser.GrpContext):
        pass

    # Exit a parse tree produced by PJPParser#Grp.
    def exitGrp(self, ctx:PJPParser.GrpContext):
        pass


    # Enter a parse tree produced by PJPParser#Mul.
    def enterMul(self, ctx:PJPParser.MulContext):
        pass

    # Exit a parse tree produced by PJPParser#Mul.
    def exitMul(self, ctx:PJPParser.MulContext):
        pass


    # Enter a parse tree produced by PJPParser#LogOr.
    def enterLogOr(self, ctx:PJPParser.LogOrContext):
        pass

    # Exit a parse tree produced by PJPParser#LogOr.
    def exitLogOr(self, ctx:PJPParser.LogOrContext):
        pass


    # Enter a parse tree produced by PJPParser#Var.
    def enterVar(self, ctx:PJPParser.VarContext):
        pass

    # Exit a parse tree produced by PJPParser#Var.
    def exitVar(self, ctx:PJPParser.VarContext):
        pass


    # Enter a parse tree produced by PJPParser#Int.
    def enterInt(self, ctx:PJPParser.IntContext):
        pass

    # Exit a parse tree produced by PJPParser#Int.
    def exitInt(self, ctx:PJPParser.IntContext):
        pass


    # Enter a parse tree produced by PJPParser#Comp.
    def enterComp(self, ctx:PJPParser.CompContext):
        pass

    # Exit a parse tree produced by PJPParser#Comp.
    def exitComp(self, ctx:PJPParser.CompContext):
        pass


    # Enter a parse tree produced by PJPParser#LogAnd.
    def enterLogAnd(self, ctx:PJPParser.LogAndContext):
        pass

    # Exit a parse tree produced by PJPParser#LogAnd.
    def exitLogAnd(self, ctx:PJPParser.LogAndContext):
        pass


    # Enter a parse tree produced by PJPParser#LogNeg.
    def enterLogNeg(self, ctx:PJPParser.LogNegContext):
        pass

    # Exit a parse tree produced by PJPParser#LogNeg.
    def exitLogNeg(self, ctx:PJPParser.LogNegContext):
        pass


    # Enter a parse tree produced by PJPParser#Str.
    def enterStr(self, ctx:PJPParser.StrContext):
        pass

    # Exit a parse tree produced by PJPParser#Str.
    def exitStr(self, ctx:PJPParser.StrContext):
        pass


    # Enter a parse tree produced by PJPParser#Div.
    def enterDiv(self, ctx:PJPParser.DivContext):
        pass

    # Exit a parse tree produced by PJPParser#Div.
    def exitDiv(self, ctx:PJPParser.DivContext):
        pass


    # Enter a parse tree produced by PJPParser#Concat.
    def enterConcat(self, ctx:PJPParser.ConcatContext):
        pass

    # Exit a parse tree produced by PJPParser#Concat.
    def exitConcat(self, ctx:PJPParser.ConcatContext):
        pass


    # Enter a parse tree produced by PJPParser#Float.
    def enterFloat(self, ctx:PJPParser.FloatContext):
        pass

    # Exit a parse tree produced by PJPParser#Float.
    def exitFloat(self, ctx:PJPParser.FloatContext):
        pass


    # Enter a parse tree produced by PJPParser#Bool.
    def enterBool(self, ctx:PJPParser.BoolContext):
        pass

    # Exit a parse tree produced by PJPParser#Bool.
    def exitBool(self, ctx:PJPParser.BoolContext):
        pass


    # Enter a parse tree produced by PJPParser#Rel.
    def enterRel(self, ctx:PJPParser.RelContext):
        pass

    # Exit a parse tree produced by PJPParser#Rel.
    def exitRel(self, ctx:PJPParser.RelContext):
        pass


    # Enter a parse tree produced by PJPParser#AriNeg.
    def enterAriNeg(self, ctx:PJPParser.AriNegContext):
        pass

    # Exit a parse tree produced by PJPParser#AriNeg.
    def exitAriNeg(self, ctx:PJPParser.AriNegContext):
        pass


    # Enter a parse tree produced by PJPParser#Assign.
    def enterAssign(self, ctx:PJPParser.AssignContext):
        pass

    # Exit a parse tree produced by PJPParser#Assign.
    def exitAssign(self, ctx:PJPParser.AssignContext):
        pass



del PJPParser