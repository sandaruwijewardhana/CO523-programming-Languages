import unittest
from src.lexer import Lexer


class TestLexer(unittest.TestCase):
    def test_keywords_and_identifiers(self):
        source = "int x; float y; if (x) else printf(x);"
        tokens = Lexer(source).tokenize()
        types = [t.type for t in tokens]
        self.assertIn("INT", types)
        self.assertIn("FLOAT", types)
        self.assertIn("IF", types)
        self.assertIn("ELSE", types)
        self.assertIn("PRINTF", types)
        self.assertIn("IDENT", types)

    def test_numbers(self):
        source = "x = 123; y = 12.34;"
        tokens = Lexer(source).tokenize()
        literals = [t.literal for t in tokens if t.type in ("INT_LIT", "FLOAT_LIT")]
        self.assertIn(123, literals)
        self.assertIn(12.34, literals)

    def test_operators(self):
        source = "x==1; x=2+3*4/5-6;"
        tokens = Lexer(source).tokenize()
        types = [t.type for t in tokens]
        self.assertIn("EQEQ", types)
        self.assertIn("EQ", types)
        self.assertIn("PLUS", types)
        self.assertIn("STAR", types)
        self.assertIn("SLASH", types)
        self.assertIn("MINUS", types)


if __name__ == "__main__":
    unittest.main()
