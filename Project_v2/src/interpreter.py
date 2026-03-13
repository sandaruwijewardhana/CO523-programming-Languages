from dataclasses import dataclass
from typing import List, Optional
from .ast_nodes import (
    Program, Block, Declaration, Assignment, IfStmt, PrintfStmt,
    Binary, Unary, Literal, Variable
)
from .errors import CLSemanticError


@dataclass
class Symbol:
    var_type: str
    value: Optional[object] = None
    initialized: bool = False


class Environment:
    def __init__(self):
        self.scopes: List[dict] = [dict()]

    def push(self):
        self.scopes.append(dict())

    def pop(self):
        self.scopes.pop()

    def declare(self, name: str, var_type: str):
        if name in self.scopes[-1]:
            raise CLSemanticError(f"Redeclaration of '{name}' in same scope.")
        self.scopes[-1][name] = Symbol(var_type)

    def assign(self, name: str, value, value_type: str):
        sym = self._resolve(name)
        if sym is None:
            raise CLSemanticError(f"Undeclared variable '{name}'.")

        if sym.var_type == "int" and value_type == "float":
            raise CLSemanticError(f"Cannot assign float to int variable '{name}'.")

        if sym.var_type == "float" and value_type == "int":
            value = float(value)
            value_type = "float"

        sym.value = value
        sym.initialized = True

    def get(self, name: str):
        sym = self._resolve(name)
        if sym is None:
            raise CLSemanticError(f"Undeclared variable '{name}'.")
        if not sym.initialized:
            raise CLSemanticError(f"Variable '{name}' used before initialization.")
        return sym.value, sym.var_type

    def _resolve(self, name: str) -> Optional[Symbol]:
        for scope in reversed(self.scopes):
            if name in scope:
                return scope[name]
        return None


class Interpreter:
    def __init__(self):
        self.env = Environment()

    def run(self, program: Program):
        self._execute(program)

    def _execute(self, node):
        if isinstance(node, Program):
            for item in node.items:
                self._execute(item)
            return

        if isinstance(node, Block):
            self.env.push()
            try:
                for item in node.items:
                    self._execute(item)
            finally:
                self.env.pop()
            return

        if isinstance(node, Declaration):
            self.env.declare(node.name, node.var_type)
            return

        if isinstance(node, Assignment):
            value, value_type = self._evaluate(node.expr)
            self.env.assign(node.name, value, value_type)
            return

        if isinstance(node, IfStmt):
            cond_value, cond_type = self._evaluate(node.condition)
            truthy = cond_value != 0
            if truthy:
                self._execute(node.then_branch)
            elif node.else_branch is not None:
                self._execute(node.else_branch)
            return

        if isinstance(node, PrintfStmt):
            value, _ = self._evaluate(node.expr)
            print(value)
            return

        raise CLSemanticError(f"Unknown statement type: {type(node)}")

    def _evaluate(self, node):
        if isinstance(node, Literal):
            return node.value, node.lit_type

        if isinstance(node, Variable):
            return self.env.get(node.name)

        if isinstance(node, Unary):
            value, value_type = self._evaluate(node.expr)
            if node.op == '-':
                return -value, value_type
            if node.op == '+':
                return +value, value_type
            raise CLSemanticError(f"Unknown unary operator '{node.op}'.")

        if isinstance(node, Binary):
            left_val, left_type = self._evaluate(node.left)
            right_val, right_type = self._evaluate(node.right)

            if node.op in ('+', '-', '*', '/'):
                result_type = "float" if left_type == "float" or right_type == "float" else "int"
                if result_type == "float":
                    left_val = float(left_val)
                    right_val = float(right_val)
                if node.op == '+':
                    return left_val + right_val, result_type
                if node.op == '-':
                    return left_val - right_val, result_type
                if node.op == '*':
                    return left_val * right_val, result_type
                if node.op == '/':
                    if result_type == "int":
                        return int(left_val / right_val), "int"
                    return left_val / right_val, "float"

            if node.op in ('>', '<', '=='):
                if node.op == '>':
                    return (1 if left_val > right_val else 0), "int"
                if node.op == '<':
                    return (1 if left_val < right_val else 0), "int"
                if node.op == '==':
                    return (1 if left_val == right_val else 0), "int"

            raise CLSemanticError(f"Unknown binary operator '{node.op}'.")

        raise CLSemanticError(f"Unknown expression type: {type(node)}")
