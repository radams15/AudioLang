import sys

import translator

class Executor:
    def __init__(self):
        self.commands = translator.executor_commands

    def _in(self):
        return sys.stdin.read(1)

    def execute(self, code):
        code = self.cleanup(list(code))
        bracemap = self.buildbracemap(code)

        cells, codeptr, cellptr = [0], 0, 0

        while codeptr < len(code):
            command = code[codeptr]

            if command == self.commands[5]:
                cellptr += 1
                if cellptr == len(cells): cells.append(0)

            if command == self.commands[4]:
                cellptr = 0 if cellptr <= 0 else cellptr - 1

            if command == self.commands[6]:
                cells[cellptr] = cells[cellptr] + 1 if cells[cellptr] < 255 else 0

            if command == self.commands[7]:
                cells[cellptr] = cells[cellptr] - 1 if cells[cellptr] > 0 else 255

            if command == self.commands[2] and cells[cellptr] == 0: codeptr = bracemap[codeptr]
            if command == self.commands[3] and cells[cellptr] != 0: codeptr = bracemap[codeptr]
            if command == self.commands[0]: sys.stdout.write(chr(cells[cellptr]))
            if command == self.commands[1]: cells[cellptr] = ord(self._in())

            codeptr += 1
        print()

    def cleanup(self, code):
        #return ''.join(filter(lambda x: x in self.commands, code))
        return list(filter(lambda x: x in self.commands, code))

    def buildbracemap(self, code):
        temp_bracestack, bracemap = [], {}

        for position, command in enumerate(code):
            if command == self.commands[2]: temp_bracestack.append(position)
            if command == self.commands[3]:
                start = temp_bracestack.pop()
                bracemap[start] = position
                bracemap[position] = start

        return bracemap