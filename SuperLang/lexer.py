from tokens import Token

class Lexer:
    KEYWORDS = ['let', 'equal', 'plus', 'minus', 'times', 'divide', 'if', 'else', 'repeat', 'say', 'do', 'greater_than']

    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_char = self.text[self.pos] if self.text else None

    def advance(self):
        self.pos += 1
        if self.pos < len(self.text):
            self.current_char = self.text[self.pos]
        else:
            self.current_char = None

    def generate_tokens(self):
        tokens = []
        while self.current_char is not None:
            if self.current_char.isspace():
                self.advance()
            elif self.current_char.isalpha():
                tokens.append(self.generate_word())
            elif self.current_char.isdigit():
                tokens.append(self.generate_number())
            elif self.current_char == '"':
                tokens.append(self.generate_string())
            else:
                self.advance()
        return tokens

    def generate_word(self):
        word = ''
        while self.current_char is not None and (self.current_char.isalnum() or self.current_char == '_'):
            word += self.current_char
            self.advance()

        if word in self.KEYWORDS:
            return Token(word.upper())
        return Token('IDENTIFIER', word)

    def generate_number(self):
        number = ''
        while self.current_char is not None and self.current_char.isdigit():
            number += self.current_char
            self.advance()
        return Token('NUMBER', int(number))

    def generate_string(self):
        self.advance()
        string = ''
        while self.current_char is not None and self.current_char != '"':
            string += self.current_char
            self.advance()
        self.advance()
        return Token('STRING', string)
