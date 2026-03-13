import sys
from .lexer import Lexer
from .parser import Parser
from .interpreter import Interpreter
from .errors import CLLexError, CLParseError, CLSemanticError


def run_source(source: str):
    tokens = Lexer(source).tokenize()
    program = Parser(tokens).parse()
    Interpreter().run(program)


def main(argv=None):
    argv = argv or sys.argv[1:]
    if len(argv) != 1:
        print("Usage: python -m src.main <file.cl>")
        return 2

    path = argv[0]
    try:
        with open(path, 'r', encoding='utf-8') as f:
            source = f.read()
        run_source(source)
        return 0
    except (CLLexError, CLParseError, CLSemanticError) as e:
        print(f"Error: {e}")
        return 1
    except FileNotFoundError:
        print(f"Error: file not found: {path}")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
