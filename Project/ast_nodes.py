class AST:
    pass

class BinOp(AST):
    def __init__(self, left, op, right):
        self.left = left
        self.token = self.op = op
        self.right = right

class UnaryOp(AST):
    def __init__(self, op, expr):
        self.token = self.op = op
        self.expr = expr

class Literal(AST):
    def __init__(self, token):
        self.token = token
        self.value = token.value

class Var(AST):
    def __init__(self, token):
        self.token = token
        self.value = token.value

class Assign(AST):
    def __init__(self, left, op, right):
        self.left = left
        self.token = self.op = op
        self.right = right

class VarDecl(AST):
    def __init__(self, type_node, var_node):
        self.type_node = type_node
        self.var_node = var_node

class Type(AST):
    def __init__(self, token):
        self.token = token
        self.value = token.value

class IfStmt(AST):
    def __init__(self, condition, then_branch, else_branch=None):
        self.condition = condition
        self.then_branch = then_branch
        self.else_branch = else_branch

class PrintStmt(AST):
    def __init__(self, var_node):
        self.var_node = var_node

class Block(AST):
    def __init__(self):
        self.children = []

class Program(AST):
    def __init__(self):
        self.children = []
