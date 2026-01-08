import re

# Define keywords and built-ins for token classification
KEYWORDS = {
    "int", "float", "char", "if", "else", "while", "for",
    "return", "void", "include", "double"
}

BUILTINS = {
    "printf", "scanf", "main", "exit", "sqrt"
}

def simple_lexer(code: str):
    """
    Simple lexical analyzer for a small subset of C.
    Prints a token table: TOKEN TYPE | VALUE

    :param code: A string of C code to analyze.
    """

    # Token specification with regex patterns for different token types
    token_specification = [
        # Order matters (longer / more specific first)
        ("COMMENT",   r"//[^\n]*"),                 # Single-line comment
        ("PREPROC",   r"\#(?:include|define)\b"),   # #include or #define

        ("STRING",    r"\"([^\"\\]|\\.)*\""),       # "Hello World" (handles escapes)
        ("FLOAT",     r"\d+\.\d+"),                 # 3.14, 11.9
        ("NUMBER",    r"\d+"),                      # 100, 25

        ("COMP",      r"==|!=|<=|>="),              # Comparison operators
        ("ASSIGN",    r"="),                        # Assignment operator

        ("OPERATOR",  r"[+\-*/%<>]"),               # Arithmetic and relational operators
        ("LBRACE",    r"\{"),                       # Left brace
        ("RBRACE",    r"\}"),                       # Right brace
        ("LPAREN",    r"\("),                       # Left parenthesis
        ("RPAREN",    r"\)"),                       # Right parenthesis
        ("COMMA",     r","),                        # Comma
        ("END",       r";"),                        # End statement (semicolon)
        ("DOT",       r"\."),                       # Dot (for object access)

        ("ID",        r"[A-Za-z_][A-Za-z0-9_]*"),   # Identifiers
        ("SKIP",      r"[ \t\r\n]+"),               # Whitespace (to be ignored)
        ("MISMATCH",  r"."),                        # Any other single char gives error
    ]

    # Compile all the regex patterns into one master regex
    tok_regex = "|".join(f"(?P<{name}>{pattern})" for name, pattern in token_specification)

    # Output header for the token table
    print(f"{'TOKEN TYPE':<12} | VALUE")
    print("-" * 28)

    # Perform the matching and processing
    for match in re.finditer(tok_regex, code):
        kind = match.lastgroup    # Get the token type
        value = match.group()     # Get the matched value

        # Skip comments and whitespace
        if kind in ("SKIP", "COMMENT"):
            continue

        # Handle identifiers: check if they are keywords or built-in functions
        if kind == "ID":
            if value in KEYWORDS:
                kind = "KEYWORD"
            elif value in BUILTINS:
                kind = "BUILTIN"

        # Handle unexpected characters
        if kind == "MISMATCH":
            print(f"Error: Unexpected char {value!r}")
        else:
            print(f"{kind:<12} | {value}")

# Test cases to check functionality
if __name__ == "__main__":
    print("\n--- Test Case 1 ---")
    simple_lexer("int a = 5 / 2;")

    print("\n--- Test Case 2 ---")
    simple_lexer("float x = 10.5; if (x >= 10) { x = x + 1; }")

    print("\n--- Test Case 3 ---")
    code3 = """#include <stdio.h>
int main() {
    printf("Hello World");
    return 0;
}
"""
    simple_lexer(code3)
