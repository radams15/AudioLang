import sys

class Executor:
    def __init__(self):
        self.max_data_size = 255
        self.mem_siz = 100000
        self.commands = [".", ",", "[", "]", "<", ">", "+", "-"] #out, in, loop start, loop end, pointer decrement, pointer increment, cell increment, cell decrement

    def _build_brace_map(self, code: str) -> dict:
        temp_brace_stack, brace_map = [], {}

        for position, command in enumerate(code):
            if command == "[": temp_brace_stack.append(position)
            if command == "]":
                start = temp_brace_stack.pop()
                brace_map[start] = position
                brace_map[position] = start
        del temp_brace_stack
        return brace_map

    def _out(self, data: str):
        return sys.stdout.write(data)
        #print(data, end="")

    def _in(self, amount):
        return sys.stdin.read(amount)
        #return input()[amount]


    def _interpret(self, data: list, debug):
        code_map = []

        for op in data:
            if op in self.commands:
                code_map.append(op)

        brace_map = self._build_brace_map(''.join(code_map))

        if debug:
            print(f"Build Bracemap : {brace_map}")

        cell_map = [0] * self.mem_siz
        operation_ptr = 0
        cell_ptr = 0

        while operation_ptr < len(code_map):
            command = code_map[operation_ptr]

            if debug:
                print(f"Command:  {command}")

            if command == self.commands[5]:
                cell_ptr += 1

            elif command == self.commands[4]:
                cell_ptr -= 1

            elif command == self.commands[6]:
                cell_map[cell_ptr] += 1

                if cell_map[cell_ptr] > self.max_data_size:
                    cell_map[cell_ptr] = 0

            elif command == self.commands[7]:
                cell_map[cell_ptr] -= 1

                if cell_map[cell_ptr] < 0:
                    cell_map[cell_ptr] = self.max_data_size

            elif command == self.commands[0]:
                self._out(chr(cell_map[cell_ptr]))

            elif command == self.commands[1]:
                cell_map[cell_ptr] = ord(self._in(1))

            elif command == self.commands[2] and cell_map[cell_ptr] == 0:
                operation_ptr = brace_map[operation_ptr]

            elif command == self.commands[3] and cell_map[cell_ptr] != 0:
                operation_ptr = brace_map[operation_ptr]

            operation_ptr += 1

        if debug:
            print(f"Final Memory: {cell_map}")
            print(cell_map[0:14])

    def execute(self, data, debug=False):
        self._interpret(data, debug=debug)