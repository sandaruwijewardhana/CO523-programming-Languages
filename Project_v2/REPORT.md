# CO523 - C-Lite Interpreter Report

## Overview
This project implements an interpreter for a simplified C-Lite language. The pipeline mirrors a classic compiler/interpreter flow:
1. Lexical analysis converts raw source characters into a stream of tokens.
2. Syntax analysis parses tokens into an Abstract Syntax Tree (AST) that encodes structure and precedence.
3. Semantic evaluation executes the AST while enforcing type rules and scope rules using a symbol table.

## Objectives Mapped to Implementation
- Translation process: `src/lexer.py`, `src/parser.py`, `src/interpreter.py` show the end-to-end flow from source to execution.
- Lexical analyzer: `Lexer` converts source into tokens (keywords, identifiers, literals, operators, delimiters).
- Syntax analysis: `Parser` validates grammar and builds AST nodes.
- Semantic evaluation: `Interpreter` executes AST and enforces semantic rules with a symbol table.
- Imperative control structures: assignments, blocks, and `if/else` are executed in order.
- Standard I/O: `printf(expr);` prints evaluated values to stdout.

## Language Definition (Implemented)
- Types: `int`, `float`
- Declarations required before use: `int x;` / `float y;`
- Assignment: `=`
- Arithmetic: `+ - * /`
- Comparison: `> < ==`
- Symbols: `(` `)` `{` `}` `;`
- Control: sequential statements, `if (...) stmt else stmt`
- Output: `printf(expr);`

## Grammar (EBNF)
```
program        ::= decl_or_stmt* EOF

decl_or_stmt   ::= declaration | statement

declaration    ::= type IDENT ";"
type           ::= "int" | "float"

statement      ::= block
                 | assignment ";"
                 | if_stmt
                 | printf_stmt ";"

block          ::= "{" decl_or_stmt* "}"

assignment     ::= IDENT "=" expr

if_stmt        ::= "if" "(" expr ")" statement ("else" statement)?

printf_stmt    ::= "printf" "(" expr ")"

expr           ::= equality
equality       ::= comparison ( "==" comparison )*
comparison     ::= term ( (">" | "<") term )*
term           ::= factor ( ("+" | "-") factor )*
factor         ::= unary ( ("*" | "/") unary )*
unary          ::= ("+" | "-") unary | primary
primary        ::= NUMBER | IDENT | "(" expr ")"

NUMBER         ::= INT_LIT | FLOAT_LIT
```

## Design Discussion
### Operator Precedence
Implemented with recursive-descent functions in `Parser`, ordered by precedence:
`equality -> comparison -> term -> factor -> unary -> primary`.
This ensures `*` and `/` bind tighter than `+` and `-`, and comparisons bind looser than arithmetic.

### Scoping Rules
Block scopes are implemented with a stack of dictionaries in `Environment`. Variables declared in a block shadow outer declarations. Redeclaration in the same scope is rejected.
Each `{ ... }` pushes a new scope. When leaving a block, the scope is popped, restoring outer bindings.

### Type Rules
- Assigning `int` to `float` is allowed (promoted to float).
- Assigning `float` to `int` is not allowed (semantic error).
- Arithmetic results are `float` if any operand is `float`, otherwise `int`.
- Division of two `int` values returns truncated `int` (C-like behavior).
- Comparisons return `int` (`1` for true, `0` for false).
These rules are enforced in `Environment.assign` and in binary expression evaluation in `Interpreter`.

### Error Handling
- Lexical errors: invalid characters, with line/column.
- Syntax errors: unexpected tokens, missing delimiters.
- Semantic errors: undeclared variable, use before initialization, redeclaration, type mismatch.
Errors are raised with descriptive messages and halt execution.

## Implementation Structure
- `src/lexer.py`: tokenization
- `src/parser.py`: parsing + AST creation
- `src/ast_nodes.py`: AST classes
- `src/interpreter.py`: execution + symbol table
- `src/errors.py`: error types
- `src/main.py`: CLI entrypoint

## Test Suite
Unit tests are in `tests/` using `unittest`. The suite includes both positive and negative cases.

### Lexer Tests
- Keywords and identifiers:
  - Input: `int x; float y; if (x) else printf(x);`
  - Ensures tokens: `INT`, `FLOAT`, `IF`, `ELSE`, `PRINTF`, `IDENT`
- Numeric literals:
  - Input: `x = 123; y = 12.34;`
  - Ensures `INT_LIT` literal `123` and `FLOAT_LIT` literal `12.34`
- Operators and delimiters:
  - Input: `x==1; x=2+3*4/5-6;`
  - Ensures `EQEQ`, `EQ`, `PLUS`, `STAR`, `SLASH`, `MINUS`
- Suggested additional lexer tests (manual or future):
  - Invalid character: `x = 1 @ 2;` should raise lexical error
  - Identifier edge: `_x1 = 0;` should tokenize as `IDENT`

### Parser Tests
- Declarations:
  - Input: `int x;` parses to one declaration node
- Assignments + precedence:
  - Input: `int x; x = 1 + 2 * 3;` parses with `*` inside `+`
- If/else parsing:
  - Input: `int x; if (x < 1) x = 2; else x = 3;`
- Block parsing:
  - Input: `{ int x; x = 1; }`
- Suggested additional parser tests:
  - Missing semicolon: `int x` should raise syntax error
  - Nested blocks: `{ int x; { int y; } }`

### Interpreter Tests
- Arithmetic evaluation:
  - Input: `int x; x = 2 + 3; printf(x);` output `5`
- Floating-point arithmetic:
  - Input: `float y; y = 1.5 * 2; printf(y);` output `3.0`
- If/else execution:
  - Input: `int x; x = 1; if (x == 1) printf(10); else printf(20);` output `10`
- Block scoping and shadowing:
  - Input:
    ```
    int x; x = 1;
    { int x; x = 2; printf(x); }
    printf(x);
    ```
  - Output lines: `2` then `1`
- Undeclared variable:
  - Input: `x = 1;` raises semantic error
- Suggested additional interpreter tests:
  - Use before initialization: `int x; printf(x);` should raise semantic error
  - Type mismatch: `int x; x = 1.5;` should raise semantic error
  - Comparison truthiness: `int x; x = 0; if (x) printf(1); else printf(2);` outputs `2`
  - Mixed arithmetic promotion:
    - Input: `int x; float y; x = 2; y = x + 0.5; printf(y);`
    - Output: `2.5`

## How to Run
Run an example program:
```
python -m src.main examples/arithmetic.cl
```

Run tests:
```
python -m unittest discover -s tests
```

## Deliverables Checklist
- Source Code: `src/`
- Grammar Specification: section above
- Design Discussion: section above
- Test Suite: `tests/` with unit and integration coverage
- Sample Programs: `examples/`
