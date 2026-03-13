from scanner import TokenType
from ast_nodes import *

class Parser:
    def __init__(self, scanner):
        self.scanner = scanner
        self.current_token = self.scanner.get_next_token()

    def error(self, message="Invalid syntax"):
        raise Exception(f"{message} at {self.current_token.line}:{self.current_token.column} (Found {self.current_token.type})")

    def eat(self, token_type):
        if self.current_token.type == token_type:
            self.current_token = self.scanner.get_next_token()
        else:
            self.error(f"Expected {token_type}")

    def program(self):
        """program ::= { statement }"""
        root = Program()
        while self.current_token.type != TokenType.EOF:
            root.children.append(self.statement())
        return root

    def statement(self):
        """statement ::= declaration | assignment | if_statement | print_statement | compound_statement"""
        if self.current_token.type in (TokenType.INT, TokenType.FLOAT):
            return self.declaration()
        elif self.current_token.type == TokenType.ID:
            return self.assignment()
        elif self.current_token.type == TokenType.IF:
            return self.if_statement()
        elif self.current_token.type == TokenType.PRINTF:
            return self.print_statement()
        elif self.current_token.type == TokenType.LBRACE:
            return self.compound_statement()
        else:
            self.error("Expected statement")

    def declaration(self):
        """declaration ::= type identifier ';'"""
        type_node = self.type_spec()
        var_node = Var(self.current_token)
        self.eat(TokenType.ID)
        self.eat(TokenType.SEMICOLON)
        return VarDecl(type_node, var_node)

    def type_spec(self):
        """type ::= 'int' | 'float'"""
        token = self.current_token
        if token.type == TokenType.INT:
            self.eat(TokenType.INT)
        else:
            self.eat(TokenType.FLOAT)
        return Type(token)

    def assignment(self):
        """assignment ::= identifier '=' expression ';'"""
        left = Var(self.current_token)
        self.eat(TokenType.ID)
        op = self.current_token
        self.eat(TokenType.ASSIGN)
        right = self.expression()
        self.eat(TokenType.SEMICOLON)
        return Assign(left, op, right)

    def if_statement(self):
        """if_statement ::= 'if' '(' comparison ')' statement [ 'else' statement ]"""
        self.eat(TokenType.IF)
        self.eat(TokenType.LPAREN)
        condition = self.comparison()
        self.eat(TokenType.RPAREN)
        then_branch = self.statement()
        else_branch = None
        if self.current_token.type == TokenType.ELSE:
            self.eat(TokenType.ELSE)
            else_branch = self.statement()
        return IfStmt(condition, then_branch, else_branch)

    def print_statement(self):
        """print_statement ::= 'printf' '(' identifier ')' ';'"""
        self.eat(TokenType.PRINTF)
        self.eat(TokenType.LPAREN)
        var_node = Var(self.current_token)
        self.eat(TokenType.ID)
        self.eat(TokenType.RPAREN)
        self.eat(TokenType.SEMICOLON)
        return PrintStmt(var_node)

    def compound_statement(self):
        """compound_statement ::= '{' { statement } '}'"""
        self.eat(TokenType.LBRACE)
        nodes = Block()
        while self.current_token.type != TokenType.RBRACE:
            nodes.children.append(self.statement())
        self.eat(TokenType.RBRACE)
        return nodes

    def comparison(self):
        """comparison ::= expression ( '>' | '<' | '==' ) expression"""
        node = self.expression()
        if self.current_token.type in (TokenType.GT, TokenType.LT, TokenType.EQ):
            op = self.current_token
            self.eat(op.type)
            node = BinOp(left=node, op=op, right=self.expression())
        return node

    def expression(self):
        """expression ::= term { ( '+' | '-' ) term }"""
        node = self.term()
        while self.current_token.type in (TokenType.PLUS, TokenType.MINUS):
            token = self.current_token
            if token.type == TokenType.PLUS:
                self.eat(TokenType.PLUS)
            elif token.type == TokenType.MINUS:
                self.eat(TokenType.MINUS)
            node = BinOp(left=node, op=token, right=self.term())
        return node

    def term(self):
        """term ::= factor { ( '*' | '/' ) factor }"""
        node = self.factor()
        while self.current_token.type in (TokenType.MUL, TokenType.DIV):
            token = self.current_token
            if token.type == TokenType.MUL:
                self.eat(TokenType.MUL)
            elif token.type == TokenType.DIV:
                self.eat(TokenType.DIV)
            node = BinOp(left=node, op=token, right=self.factor())
        return node

    def factor(self):
        """factor ::= identifier | float_literal | int_literal | '(' expression ')'"""
        token = self.current_token
        if token.type == TokenType.ID:
            self.eat(TokenType.ID)
            return Var(token)
        elif token.type == TokenType.INT_LITERAL:
            self.eat(TokenType.INT_LITERAL)
            return Literal(token)
        elif token.type == TokenType.FLOAT_LITERAL:
            self.eat(TokenType.FLOAT_LITERAL)
            return Literal(token)
        elif token.type == TokenType.LPAREN:
            self.eat(TokenType.LPAREN)
            node = self.expression()
            self.eat(TokenType.RPAREN)
            return node
        else:
            self.error("Expected identifier, literal, or '('")

    def parse(self):
        node = self.program()
        if self.current_token.type != TokenType.EOF:
            self.error("End of file expected")
        return node
