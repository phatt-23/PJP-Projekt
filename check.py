from typing import Literal, Union
import expr
from stmt import *
import stmt

Type = Literal['int', 'float', 'string', 'bool', None]

def is_num_type(t: Type):
    return t in ['int', 'float']


class Checker():
    vars: dict[str, Type] = {}  # id, type
    errs = []

    def type_check(self, prog: list[Stmt]):
        for st in prog:
            self.check_stmt(st)

        return self.errs

    def check_stmt(self, st: Stmt):
        match st:
            case stmt.ExprStmt():
                self.check_expr(st.expr)

            case stmt.Decl(type=t, ids=ids):
                for id in ids:
                    if id in self.vars:
                        if t != self.vars[id]:
                            self.errs.append(f"Tried to decl var '{id}' with type '{t}' but it's already declared with type of '{self.vars[id]}'.")
                    else:
                        self.vars[id] = t

            case stmt.Read():
                pass

            case stmt.Write():
                for e in st.exprs:
                    self.check_expr(e)

            case stmt.Block():
                for s in st.stmts:
                    self.check_stmt(s)

            case stmt.Cond():
                self.check_expr(st.expr)
                self.check_stmt(st.then)
                if st.otherwise != None:
                    self.check_stmt(st.otherwise) 

            case stmt.Cycle():
                self.check_expr(st.expr)
                self.check_stmt(st.body)


    def check_expr(self, ex: Expr) -> Type:
        match ex:
            case expr.Grp():
                return self.check_expr(ex.expr)

            case expr.Una():
                return self.check_expr(ex.expr)

            case expr.Ari():
                lt = self.check_expr(ex.left)
                rt = self.check_expr(ex.right)
                if not is_num_type(lt) or not is_num_type(rt):
                    self.errs.append("Arithmetic op can only be performed on numbers.")
                    return None
                return 'float' if lt == 'float' or rt == 'float' else 'int'

            case expr.Rel():
                lt = self.check_expr(ex.left)
                rt = self.check_expr(ex.right)
                allowed = ['int', 'float', 'string']
                if lt not in allowed or rt not in allowed :
                    self.errs.append("Rel op can only be performed on numbers and strings.")
                    return None
                return lt

            case expr.Comp():
                lt = self.check_expr(ex.left)
                rt = self.check_expr(ex.right)
                if lt != rt:
                    self.errs.append("Comp op can be performed only for the same type.")
                    return None;
                return lt

            case expr.Concat():
                lt = self.check_expr(ex.left)
                rt = self.check_expr(ex.right)
                print('concat', lt, rt)
                if rt != lt != 'string':
                    self.errs.append("Concat can be performed only on strings.")
                    return None;
                return lt

            case expr.Log():
                lt = self.check_expr(ex.left)
                rt = self.check_expr(ex.right)
                if rt != lt != 'bool':
                    self.errs.append("Concat can be performed only on bools.")
                    return None
                return lt

            case expr.Assign():
                lt = self.vars[ex.id]
                rt = self.check_expr(ex.expr)
                if rt != lt:
                    self.errs.append(f"Can't assign expr of type '{rt}' to var '{ex.id}' of type '{lt}'.")
                    return None
                return lt

            case expr.Lit():
                v = ex.val

                if isinstance(v, bool):
                    return 'bool'
                elif isinstance(v, int):
                    return 'int'
                elif isinstance(v, float):
                    return 'float'
                elif isinstance(v, str):
                    return 'string'

                return None

            case expr.Var():
                return self.vars[ex.id]

        return None
                        

