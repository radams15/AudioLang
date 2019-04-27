import ctypes

commands = [".", ",", "[", "]", "<", ">", "+", "-"]

class Executor:
    def __init__(self):
        self.commands = commands
        self.executor = ctypes.CDLL("./libexecutor.so")

    def execute(self, data):
        code = "".join(data)
        print(code)
        str_code = ctypes.create_string_buffer(str.encode(code))
        self.executor.interpret(str_code)