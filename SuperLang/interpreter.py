
class Context:
    def __init__(self):
        self.symbols = {}
        self.functions = {}

class Interpreter:
    def __init__(self, tree):
        self.tree = tree
        self.ctx = Context()

    def visit(self, node):
        method_name = f'visit_{type(node).__name__}'
        method = getattr(self, method_name, self.no_visit_method)
        return method(node)

    def no_visit_method(self, node):
        raise Exception(f"No visit_{type(node).__name__} method.")

    def interpret(self):
        for statement in self.tree:
            self.visit(statement)

    def visit_NumberNode(self, node):
        return node.value

    def visit_StringNode(self, node):
        return node.value

    def visit_VarAccessNode(self, node):
        return self.ctx.symbols.get(node.name, 0)

    def visit_VarAssignNode(self, node):
        value = self.visit(node.value)
        self.ctx.symbols[node.name] = value
        return value

    def visit_BinOpNode(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)

        if node.op == 'PLUS':
            if isinstance(left, str) or isinstance(right, str):
                return str(left) + str(right)
            return left + right
        if node.op == 'MINUS':
            return left - right
        if node.op == 'TIMES':
            return left * right
        if node.op == 'DIVIDE':
            return left / right
        if node.op == 'GREATER_THAN':
            return left > right

    def visit_SayNode(self, node):
        value = self.visit(node.value)
        print(value)

    def visit_IfNode(self, node):
        condition = self.visit(node.condition)
        if condition:
            for stmt in node.true_block:
                self.visit(stmt)
        else:
            for stmt in node.false_block:
                self.visit(stmt)

    def visit_RepeatNode(self, node):
        times = self.visit(node.times)
        for _ in range(times):
            for stmt in node.block:
                self.visit(stmt)

    def visit_FuncDefNode(self, node):
        self.ctx.functions[node.name] = (node.param, node.body)

    def visit_FuncCallNode(self, node):
        func = self.ctx.functions.get(node.name)
        if func is None:
            raise Exception(f"Function '{node.name}' not found.")

        param_name, body = func
        arg_value = self.visit(node.arg)

        backup = dict(self.ctx.symbols)
        self.ctx.symbols[param_name] = arg_value
        for stmt in body:
            self.visit(stmt)
        self.ctx.symbols = backup
