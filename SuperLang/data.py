class Data:
    def __init__(self):
        self.variables = {}
        self.functions = {}
    
    def read(self, id):
        if id not in self.variables:
            raise ValueError(f"Undefined variable: {id}")
        return self.variables[id]
    
    def read_all(self):
        return self.variables
    
    def write(self, variable, expression):
        variable_name = variable.value
        self.variables[variable_name] = expression
    
    def store_function(self, name, params, body):
        self.functions[name] = (params, body)
    
    def get_function(self, name):
        if name not in self.functions:
            raise ValueError(f"Undefined function: {name}")
        return self.functions[name]