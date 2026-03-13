from typing import List
from .ast_nodes import Token
from .errors import CLLexError


KEYWORDS = {
    "int": "INT",
    "float": "FLOAT",
    "if": "IF",
    "else": "ELSE",
    "printf": "PRINTF",
}

SINGLE_CHAR = {
    '+': "PLUS",
    '-': "MINUS",
    '*': "STAR",
    '/': "SLASH",
    '>': "GT",
    '<': "LT",
    '=': "EQ",
    '(': "LPAREN",
    ')': "RPAREN",
    '{': "LBRACE",
    '}': "RBRACE",
    ';': "SEMI",
}


class Lexer:
    def __init__(self, source: str):
        self.source = source
        self.tokens: List[Token] = []
        self.start = 0
        self.current = 0
        self.line = 1
        self.col = 1

    def tokenize(self) -> List[Token]:
        while not self._is_at_end():
            self.start = self.current
            self._scan_token()
        self.tokens.append(Token("EOF", "", None, self.line, self.col))
        return self.tokens

    def _is_at_end(self) -> bool:
        return self.current >= len(self.source)

    def _advance(self) -> str:
        ch = self.source[self.current]
        self.current += 1
        self.col += 1
        return ch

    def _peek(self) -> str:
        if self._is_at_end():
            return "\0"
        return self.source[self.current]

    def _match(self, expected: str) -> bool:
        if self._is_at_end():
            return False
        if self.source[self.current] != expected:
            return False
        self.current += 1
        self.col += 1
        return True

    def _add_token(self, token_type: str, literal=None):
        lexeme = self.source[self.start:self.current]
        self.tokens.append(Token(token_type, lexeme, literal, self.line, self.col - len(lexeme)))

    def _scan_token(self):
        ch = self._advance()

        if ch in (' ', '\t', '\r'):
            return
        if ch == '\n':
            self.line += 1
            self.col = 1
            return

        if ch.isalpha() or ch == '_':
            self._identifier()
            return

        if ch.isdigit():
            self._number()
            return

        if ch == '=':
            if self._match('='):
                self._add_token("EQEQ")
            else:
                self._add_token("EQ")
            return

        if ch in SINGLE_CHAR:
            self._add_token(SINGLE_CHAR[ch])
            return

        raise CLLexError(f"Unexpected character '{ch}' at line {self.line}, col {self.col - 1}")

    def _identifier(self):
        while self._peek().isalnum() or self._peek() == '_':
            self._advance()
        text = self.source[self.start:self.current]
        token_type = KEYWORDS.get(text, "IDENT")
        self._add_token(token_type)

    def _number(self):
        while self._peek().isdigit():
            self._advance()

        is_float = False
        if self._peek() == '.':
            if self.current + 1 < len(self.source) and self.source[self.current + 1].isdigit():
                is_float = True
                self._advance()  # consume '.'
                while self._peek().isdigit():
                    self._advance()

        text = self.source[self.start:self.current]
        if is_float:
            self._add_token("FLOAT_LIT", float(text))
        else:
            self._add_token("INT_LIT", int(text))
