from lexer import Lexer
from parser import Parser
from interpreter import Interpreter
from tokens import Token

def run(code):
    lexer = Lexer(code)
    tokens = lexer.generate_tokens()
    print("TOKENS:", tokens)  # <-- GOOD
    parser = Parser(tokens)
    tree = parser.parse()
    print("TREE:", tree)  # <-- GOOD
    interpreter = Interpreter(tree)
    return interpreter.interpret()
