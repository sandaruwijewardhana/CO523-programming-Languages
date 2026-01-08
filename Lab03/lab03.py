import re
# ----------------------------
# Token sets (post-processing)
# ----------------------------
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
    """

    token_specification = [
        # Order matters (longer / more specific first)
        ("COMMENT",   r"//[^\n]*"),                 # single-line comment
        ("PREPROC",   r"\#(?:include|define)\b"),    # #include or #define

        ("STRING",    r"\"([^\"\\]|\\.)*\""),       # "Hello World" (handles escapes)
        ("FLOAT",     r"\d+\.\d+"),                 # 3.14, 10.5
        ("NUMBER",    r"\d+"),                      # 10, 250

        ("COMP",      r"==|!=|<=|>="),              # comparison operators
        ("ASSIGN",    r"="),                        # assignment operator

        ("OPERATOR",  r"[+\-*/%<>]"),               # arithmetic + relational (<, >)
        ("LBRACE",    r"\{"),
        ("RBRACE",    r"\}"),
        ("LPAREN",    r"\("),
        ("RPAREN",    r"\)"),
        ("COMMA",     r","),
        ("END",       r";"),
        ("DOT",       r"\."),

        ("ID",        r"[A-Za-z_][A-Za-z0-9_]*"),   # identifiers
        ("SKIP",      r"[ \t\r\n]+"),               # whitespace
        ("MISMATCH",  r"."),                        # any other single char gives error
    ]

    #  Compile patterns into one master Regular Expression
    tok_regex = "|".join(f"(?P<{name}>{pattern})" for name, pattern in token_specification)

    print(f"{'TOKEN TYPE':<12} | VALUE")
    print("-" * 28)

    # The Scanning Loop
    for match in re.finditer(tok_regex, code):
        kind = match.lastgroup
        value = match.group()

        if kind in ("SKIP", "COMMENT"):
            continue

        # Classify identifiers as KEYWORD / BUILTIN when applicable
        if kind == "ID":
            if value in KEYWORDS:
                kind = "KEYWORD"
            elif value in BUILTINS:
                kind = "BUILTIN"

        if kind == "MISMATCH":
            print(f"Error: Unexpected char {value!r}")
        else:
            print(f"{kind:<12} | {value}")


# ----------------------------
# Test with lab examples
# ----------------------------
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
