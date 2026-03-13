from typing import List, Optional
from .ast_nodes import (
    Program, Block, Declaration, Assignment, IfStmt, PrintfStmt,
    Binary, Unary, Literal, Variable, Token
)
from .errors import CLParseError


class Parser:
    def __init__(self, tokens: List[Token]):
        self.tokens = tokens
        self.current = 0

    def parse(self) -> Program:
        items = []
        while not self._is_at_end():
            items.append(self._declaration_or_statement())
        return Program(items)

    def _declaration_or_statement(self):
        if self._match("INT", "FLOAT"):
            return self._declaration(self._previous())
        return self._statement()

    def _declaration(self, type_token: Token):
        name = self._consume("IDENT", "Expected identifier after type.")
        self._consume("SEMI", "Expected ';' after declaration.")
        return Declaration(type_token.lexeme, name.lexeme)

    def _statement(self):
        if self._match("LBRACE"):
            return self._block()
        if self._match("IF"):
            return self._if_stmt()
        if self._match("PRINTF"):
            return self._printf_stmt()

        stmt = self._assignment()
        self._consume("SEMI", "Expected ';' after assignment.")
        return stmt

    def _block(self):
        items = []
        while not self._check("RBRACE") and not self._is_at_end():
            items.append(self._declaration_or_statement())
        self._consume("RBRACE", "Expected '}' after block.")
        return Block(items)

    def _if_stmt(self):
        self._consume("LPAREN", "Expected '(' after if.")
        condition = self._expression()
        self._consume("RPAREN", "Expected ')' after if condition.")
        then_branch = self._statement()
        else_branch = None
        if self._match("ELSE"):
            else_branch = self._statement()
        return IfStmt(condition, then_branch, else_branch)

    def _printf_stmt(self):
        self._consume("LPAREN", "Expected '(' after printf.")
        expr = self._expression()
        self._consume("RPAREN", "Expected ')' after printf argument.")
        self._consume("SEMI", "Expected ';' after printf.")
        return PrintfStmt(expr)

    def _assignment(self):
        name = self._consume("IDENT", "Expected identifier at start of assignment.")
        self._consume("EQ", "Expected '=' in assignment.")
        expr = self._expression()
        return Assignment(name.lexeme, expr)

    def _expression(self):
        return self._equality()

    def _equality(self):
        expr = self._comparison()
        while self._match("EQEQ"):
            op = self._previous().lexeme
            right = self._comparison()
            expr = Binary(op, expr, right)
        return expr

    def _comparison(self):
        expr = self._term()
        while self._match("GT", "LT"):
            op = self._previous().lexeme
            right = self._term()
            expr = Binary(op, expr, right)
        return expr

    def _term(self):
        expr = self._factor()
        while self._match("PLUS", "MINUS"):
            op = self._previous().lexeme
            right = self._factor()
            expr = Binary(op, expr, right)
        return expr

    def _factor(self):
        expr = self._unary()
        while self._match("STAR", "SLASH"):
            op = self._previous().lexeme
            right = self._unary()
            expr = Binary(op, expr, right)
        return expr

    def _unary(self):
        if self._match("PLUS", "MINUS"):
            op = self._previous().lexeme
            right = self._unary()
            return Unary(op, right)
        return self._primary()

    def _primary(self):
        if self._match("INT_LIT"):
            return Literal(self._previous().literal, "int")
        if self._match("FLOAT_LIT"):
            return Literal(self._previous().literal, "float")
        if self._match("IDENT"):
            return Variable(self._previous().lexeme)
        if self._match("LPAREN"):
            expr = self._expression()
            self._consume("RPAREN", "Expected ')' after expression.")
            return expr

        raise self._error(self._peek(), "Expected expression.")

    def _match(self, *types):
        for t in types:
            if self._check(t):
                self._advance()
                return True
        return False

    def _check(self, token_type: str) -> bool:
        if self._is_at_end():
            return False
        return self._peek().type == token_type

    def _advance(self):
        if not self._is_at_end():
            self.current += 1
        return self._previous()

    def _is_at_end(self) -> bool:
        return self._peek().type == "EOF"

    def _peek(self) -> Token:
        return self.tokens[self.current]

    def _previous(self) -> Token:
        return self.tokens[self.current - 1]

    def _consume(self, token_type: str, message: str) -> Token:
        if self._check(token_type):
            return self._advance()
        raise self._error(self._peek(), message)

    def _error(self, token: Token, message: str) -> CLParseError:
        loc = f"line {token.line}, col {token.col}"
        return CLParseError(f"{message} (at {loc})")
