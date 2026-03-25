grammar PJP;

prog: stmt* EOF 
    ;

stmt: ';'                                   # Empty
    | expr ';'                              # ExprStmt
    | TYPE ID (',' ID)* ';'                 # Decl
    | 'read' ID (',' ID)* ';'               # Read
    | 'write' expr ((',' | '..') expr)* ';'          # Write
    | '{' stmt* '}'                         # Block
    | 'if' '(' expr ')' stmt ('else' stmt)? # Cond
    | 'while' '(' expr ')' stmt             # Cycle
    ;

expr: '(' expr ')'                          # Grp
    | '-' expr                              # AriNeg // N x N -> N where N = I | F
    | '!' expr                              # LogNeg // B -> B
    | expr '%' expr                         # Mod // I x I -> I
    | expr '/' expr                         # Div
    | expr '*' expr                         # Mul
    | expr '-' expr                         # Sub // implicit INT to FLOAT conversion is allowed
    | expr '+' expr                         # Add
    | expr '.' expr                         # Concat // S x S -> S
    | expr ('<' | '>') expr                 # Rel // N x N -> B where N = I | F
    | expr ('==' | '!=') expr               # Comp // X x Y -> B where X,Y = I|F|S|B and X==Y
    | expr '&&' expr                        # LogAnd // B x B -> B
    | expr '||' expr                        # LogOr // B x B -> B
    | <assoc=right> ID '=' expr             # Assign // x = a = b = 3 + 2, just in case
    | INT                                   # Int
    | FLOAT                                 # Float
    | BOOL                                  # Bool
    | STRING                                # Str
    | ID                                    # Var
    ;

TYPE    : 'int' | 'float' | 'bool' | 'string' ;
INT     : '0' | [1-9][0-9]* ;
FLOAT   : [0-9]+ '.' [0-9]+ ;
BOOL    : 'true' | 'false' ;
STRING  : '"' ~["]* '"' | '\'' ~[']* '\'' ;
ID      : [a-zA-Z][a-zA-Z_0-9]* ;
WS      : [ \t\r\n]+ -> skip ;
COMMENT : '//' ~('\r' | '\n')* -> skip ;


