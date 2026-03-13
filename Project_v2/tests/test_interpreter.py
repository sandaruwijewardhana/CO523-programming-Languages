import io
import unittest
from contextlib import redirect_stdout

from src.lexer import Lexer
from src.parser import Parser
from src.interpreter import Interpreter
from src.errors import CLSemanticError


def run_program(source: str) -> str:
    tokens = Lexer(source).tokenize()
    program = Parser(tokens).parse()
    interpreter = Interpreter()
    buf = io.StringIO()
    with redirect_stdout(buf):
        interpreter.run(program)
    return buf.getvalue().strip()


class TestInterpreter(unittest.TestCase):
    def test_arithmetic(self):
        source = "int x; x = 2 + 3; printf(x);"
        out = run_program(source)
        self.assertEqual(out, "5")

    def test_float(self):
        source = "float y; y = 1.5 * 2; printf(y);"
        out = run_program(source)
        self.assertEqual(out, "3.0")

    def test_if_else(self):
        source = "int x; x = 1; if (x == 1) printf(10); else printf(20);"
        out = run_program(source)
        self.assertEqual(out, "10")

    def test_scope(self):
        source = "int x; x = 1; { int x; x = 2; printf(x); } printf(x);"
        out = run_program(source)
        self.assertEqual(out.splitlines(), ["2", "1"])

    def test_undeclared(self):
        source = "x = 1;"
        with self.assertRaises(CLSemanticError):
            run_program(source)


if __name__ == "__main__":
    unittest.main()
