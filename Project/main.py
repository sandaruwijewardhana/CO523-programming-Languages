import sys
from scanner import Scanner
from c_lite_parser import Parser
from interpreter import Interpreter

def execute(source):
    try:
        scanner = Scanner(source)
        parser = Parser(scanner)
        tree = parser.parse()
        interpreter = Interpreter(tree)
        interpreter.interpret()
    except Exception as e:
        print(f"Error: {e}")

def main():
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as f:
            source = f.read()
        execute(source)
    else:
        print("C-Lite Interpreter")
        print("Type your code (Ctrl+D or Ctrl+Z to finish):")
        source = sys.stdin.read()
        execute(source)

if __name__ == "__main__":
    main()
