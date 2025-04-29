class Node:
    pass

class NumberNode(Node):
    def __init__(self, value):
        self.value = value

class StringNode(Node):
    def __init__(self, value):
        self.value = value

class VarAccessNode(Node):
    def __init__(self, name):
        self.name = name

class VarAssignNode(Node):
    def __init__(self, name, value):
        self.name = name
        self.value = value

class BinOpNode(Node):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

class SayNode(Node):
    def __init__(self, value):
        self.value = value

class IfNode(Node):
    def __init__(self, condition, true_block, false_block):
        self.condition = condition
        self.true_block = true_block
        self.false_block = false_block

class RepeatNode(Node):
    def __init__(self, times, block):
        self.times = times
        self.block = block

class FuncDefNode(Node):
    def __init__(self, name, param, body):
        self.name = name
        self.param = param
        self.body = body

class FuncCallNode(Node):
    def __init__(self, name, arg):
        self.name = name
        self.arg = arg

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def peek(self):
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        return None

    def advance(self):
        self.pos += 1

    def parse(self):
        print("Parsing started...")
        statements = []
        while self.peek():
            stmt = self.statement()
            if stmt is not None:
                statements.append(stmt)
            else:
                self.advance()
        print("Parsing ended.")
        return statements

    def statement(self):
        token = self.peek()

        if token is None:
            return None

        if token.type == 'LET':
            self.advance()
            var_name = self.peek()
            self.advance()
            if self.peek() and self.peek().type == 'EQUAL':
                self.advance()
            expr = self.expression()
            return VarAssignNode(var_name.value, expr)

        if token.type == 'SAY':
            self.advance()
            expr = self.expression()
            return SayNode(expr)

        if token.type == 'IF':
            self.advance()
            condition = self.expression()
            true_block = self.collect_block()
            false_block = []
            if self.peek() and self.peek().type == 'ELSE':
                self.advance()
                false_block = self.collect_block()
            return IfNode(condition, true_block, false_block)

        if token.type == 'REPEAT':
            self.advance()
            times_token = self.peek()
            if times_token.type != 'NUMBER':
                raise Exception("Expected number after 'repeat'")
            self.advance()

            if self.peek() and self.peek().type == 'TIMES':
                self.advance()

            block = self.collect_block()
            return RepeatNode(NumberNode(times_token.value), block)

        if token.type == 'DO':
            self.advance()
            func_name = self.peek()
            self.advance()
            param = self.peek()
            self.advance()
            body = self.collect_block()
            return FuncDefNode(func_name.value, param.value, body)

        if token.type == 'IDENTIFIER':
            self.advance()
            next_token = self.peek()
            if next_token and next_token.type == 'IDENTIFIER':
                func_name = token.value
                arg = VarAccessNode(next_token.value)
                self.advance()
                return FuncCallNode(func_name, arg)
            return VarAccessNode(token.value)

        return None

    def expression(self):
        node = self.term()
        while self.peek() and self.peek().type in ('PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'GREATER_THAN'):
            op_token = self.peek()
            self.advance()
            right = self.term()
            node = BinOpNode(node, op_token.type, right)
        return node

    def term(self):
        token = self.peek()
        if token.type == 'NUMBER':
            self.advance()
            return NumberNode(token.value)
        if token.type == 'STRING':
            self.advance()
            return StringNode(token.value)
        if token.type == 'IDENTIFIER':
            self.advance()
            return VarAccessNode(token.value)
        return None

    def collect_block(self):
        block = []
        while self.peek():
            token = self.peek()
            if token.type in ('ELSE', 'LET', 'IF', 'REPEAT', 'DO', 'EOF'):
                break
            stmt = self.statement()
            if stmt:
                block.append(stmt)
        return block
