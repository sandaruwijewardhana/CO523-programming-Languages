import enum

class TokenType(enum.Enum):
    # Keywords
    INT = 'int'
    FLOAT = 'float'
    IF = 'if'
    ELSE = 'else'
    PRINTF = 'printf'
    
    # Literals
    ID = 'ID'
    INT_LITERAL = 'INT_LITERAL'
    FLOAT_LITERAL = 'FLOAT_LITERAL'
    
    # Operators
    ASSIGN = '='
    PLUS = '+'
    MINUS = '-'
    MUL = '*'
    DIV = '/'
    GT = '>'
    LT = '<'
    EQ = '=='
    
    # Symbols
    LPAREN = '('
    RPAREN = ')'
    LBRACE = '{'
    RBRACE = '}'
    SEMICOLON = ';'
    
    EOF = 'EOF'

class Token:
    def __init__(self, type, value, line, column):
        self.type = type
        self.value = value
        self.line = line
        self.column = column

    def __str__(self):
        return f'Token({self.type}, {repr(self.value)}, line={self.line}, col={self.column})'

    def __repr__(self):
        return self.__str__()

class Scanner:
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.line = 1
        self.column = 1
        self.current_char = self.text[0] if len(self.text) > 0 else None

    def advance(self):
        if self.current_char == '\n':
            self.line += 1
            self.column = 0
        
        self.pos += 1
        if self.pos > len(self.text) - 1:
            self.current_char = None
        else:
            self.current_char = self.text[self.pos]
            self.column += 1

    def peek(self):
        peek_pos = self.pos + 1
        if peek_pos > len(self.text) - 1:
            return None
        else:
            return self.text[peek_pos]

    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def skip_comment(self):
        while self.current_char is not None and self.current_char != '\n':
            self.advance()

    def identifier(self):
        result = ''
        start_col = self.column
        while self.current_char is not None and (self.current_char.isalnum() or self.current_char == '_'):
            result += self.current_char
            self.advance()
        
        # Check if it's a keyword
        for token_type in TokenType:
            if token_type.value == result and token_type not in (TokenType.ID, TokenType.INT_LITERAL, TokenType.FLOAT_LITERAL):
                return Token(token_type, result, self.line, start_col)
        
        return Token(TokenType.ID, result, self.line, start_col)

    def number(self):
        result = ''
        start_col = self.column
        is_float = False
        while self.current_char is not None and (self.current_char.isdigit() or self.current_char == '.'):
            if self.current_char == '.':
                if is_float: break
                is_float = True
            result += self.current_char
            self.advance()
        
        if is_float:
            return Token(TokenType.FLOAT_LITERAL, float(result), self.line, start_col)
        return Token(TokenType.INT_LITERAL, int(result), self.line, start_col)

    def get_next_token(self):
        while self.current_char is not None:
            if self.current_char.isspace():
                self.skip_whitespace()
                continue

            if self.current_char == '/' and self.peek() == '/':
                self.skip_comment()
                continue

            if self.current_char.isalpha() or self.current_char == '_':
                return self.identifier()

            if self.current_char.isdigit():
                return self.number()

            if self.current_char == '=' and self.peek() == '=':
                start_col = self.column
                self.advance()
                self.advance()
                return Token(TokenType.EQ, '==', self.line, start_col)

            if self.current_char == '=':
                start_col = self.column
                self.advance()
                return Token(TokenType.ASSIGN, '=', self.line, start_col)

            if self.current_char == '+':
                start_col = self.column
                self.advance()
                return Token(TokenType.PLUS, '+', self.line, start_col)

            if self.current_char == '-':
                start_col = self.column
                self.advance()
                return Token(TokenType.MINUS, '-', self.line, start_col)

            if self.current_char == '*':
                start_col = self.column
                self.advance()
                return Token(TokenType.MUL, '*', self.line, start_col)

            if self.current_char == '/':
                start_col = self.column
                self.advance()
                return Token(TokenType.DIV, '/', self.line, start_col)

            if self.current_char == '>':
                start_col = self.column
                self.advance()
                return Token(TokenType.GT, '>', self.line, start_col)

            if self.current_char == '<':
                start_col = self.column
                self.advance()
                return Token(TokenType.LT, '<', self.line, start_col)

            if self.current_char == '(':
                start_col = self.column
                self.advance()
                return Token(TokenType.LPAREN, '(', self.line, start_col)

            if self.current_char == ')':
                start_col = self.column
                self.advance()
                return Token(TokenType.RPAREN, ')', self.line, start_col)

            if self.current_char == '{':
                start_col = self.column
                self.advance()
                return Token(TokenType.LBRACE, '{', self.line, start_col)

            if self.current_char == '}':
                start_col = self.column
                self.advance()
                return Token(TokenType.RBRACE, '}', self.line, start_col)

            if self.current_char == ';':
                start_col = self.column
                self.advance()
                return Token(TokenType.SEMICOLON, ';', self.line, start_col)

            raise Exception(f"Unexpected character '{self.current_char}' at {self.line}:{self.column}")

        return Token(TokenType.EOF, None, self.line, self.column)
