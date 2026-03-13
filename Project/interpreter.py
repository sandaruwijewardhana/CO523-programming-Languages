from scanner import TokenType
from ast_nodes import *

class SymbolTable:
    def __init__(self, parent=None):
        self.symbols = {}
        self.parent = parent

    def define(self, name, type, value=None):
        if name in self.symbols:
            raise Exception(f"Semantic Error: Duplicate declaration of variable '{name}'")
        self.symbols[name] = {'type': type, 'value': value}

    def assign(self, name, value):
        if name in self.symbols:
            # Type checking/enforcement could happen here
            self.symbols[name]['value'] = value
        elif self.parent:
            self.parent.assign(name, value)
        else:
            raise Exception(f"Semantic Error: Assignment to undeclared variable '{name}'")

    def lookup(self, name):
        if name in self.symbols:
            return self.symbols[name]
        elif self.parent:
            return self.parent.lookup(name)
        else:
            raise Exception(f"Semantic Error: Use of undeclared variable '{name}'")

class Interpreter:
    def __init__(self, tree):
        self.tree = tree
        self.global_scope = SymbolTable()
        self.current_scope = self.global_scope

    def visit(self, node):
        method_name = f'visit_{type(node).__name__}'
        visitor = getattr(self, method_name, self.generic_visit)
        return visitor(node)

    def generic_visit(self, node):
        raise Exception(f'No visit_{type(node).__name__} method')

    def visit_Program(self, node):
        for child in node.children:
            self.visit(child)

    def visit_Block(self, node):
        # In C-Lite, we can treat compound statements as new scopes if needed, 
        # but for simplicity as per requirements we'll maintain the current scope 
        # unless nested scoping is explicitly required for blocks.
        # Let's implement block scoping.
        previous_scope = self.current_scope
        self.current_scope = SymbolTable(parent=previous_scope)
        for child in node.children:
            self.visit(child)
        self.current_scope = previous_scope

    def visit_VarDecl(self, node):
        var_name = node.var_node.value
        var_type = node.type_node.value
        # Default values
        default_val = 0 if var_type == 'int' else 0.0
        self.current_scope.define(var_name, var_type, default_val)

    def visit_Assign(self, node):
        var_name = node.left.value
        value = self.visit(node.right)
        self.current_scope.assign(var_name, value)

    def visit_IfStmt(self, node):
        if self.visit(node.condition):
            self.visit(node.then_branch)
        elif node.else_branch:
            self.visit(node.else_branch)

    def visit_PrintStmt(self, node):
        var_name = node.var_node.value
        symbol = self.current_scope.lookup(var_name)
        print(symbol['value'])

    def visit_BinOp(self, node):
        left_val = self.visit(node.left)
        right_val = self.visit(node.right)
        op_type = node.op.type

        if op_type == TokenType.PLUS:
            return left_val + right_val
        elif op_type == TokenType.MINUS:
            return left_val - right_val
        elif op_type == TokenType.MUL:
            return left_val * right_val
        elif op_type == TokenType.DIV:
            if right_val == 0:
                raise Exception("Runtime Error: Division by zero")
            return left_val / right_val
        elif op_type == TokenType.GT:
            return left_val > right_val
        elif op_type == TokenType.LT:
            return left_val < right_val
        elif op_type == TokenType.EQ:
            return left_val == right_val

    def visit_Var(self, node):
        var_name = node.value
        return self.current_scope.lookup(var_name)['value']

    def visit_Literal(self, node):
        return node.value

    def interpret(self):
        return self.visit(self.tree)
