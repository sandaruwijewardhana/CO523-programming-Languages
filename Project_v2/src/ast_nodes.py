from dataclasses import dataclass
from typing import List, Optional


@dataclass
class Token:
    type: str
    lexeme: str
    literal: object
    line: int
    col: int


@dataclass
class Program:
    items: List[object]


@dataclass
class Block:
    items: List[object]


@dataclass
class Declaration:
    var_type: str
    name: str


@dataclass
class Assignment:
    name: str
    expr: object


@dataclass
class IfStmt:
    condition: object
    then_branch: object
    else_branch: Optional[object]


@dataclass
class PrintfStmt:
    expr: object


@dataclass
class Binary:
    op: str
    left: object
    right: object


@dataclass
class Unary:
    op: str
    expr: object


@dataclass
class Literal:
    value: object
    lit_type: str


@dataclass
class Variable:
    name: str
