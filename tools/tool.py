

class Tool:
    def __init__(
            self,
            name
    ):
        self.name = name
    def exec(self, function_name):
        method = getattr(self, function_name)
        return method()