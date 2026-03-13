import unittest
from src.lexer import Lexer
from src.parser import Parser


class TestParser(unittest.TestCase):
    def parse(self, source: str):
        tokens = Lexer(source).tokenize()
        return Parser(tokens).parse()

    def test_declaration(self):
        program = self.parse("int x;")
        self.assertEqual(len(program.items), 1)

    def test_assignment_and_expr(self):
        program = self.parse("int x; x = 1 + 2 * 3;")
        self.assertEqual(len(program.items), 2)

    def test_if_else(self):
        program = self.parse("int x; if (x < 1) x = 2; else x = 3;")
        self.assertEqual(len(program.items), 2)

    def test_block(self):
        program = self.parse("{ int x; x = 1; }")
        self.assertEqual(len(program.items), 1)


if __name__ == "__main__":
    unittest.main()
