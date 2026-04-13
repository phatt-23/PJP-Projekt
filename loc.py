from dataclasses import dataclass

class Loc():
    line: int | None 
    column: int | None 
    
    def __init__(self, line=None, column=None):
        self.line = line
        self.column = column

    def __repr__(self):
        return f"[{self.line}:{self.column}]"
