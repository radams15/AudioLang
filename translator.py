#out, in, loop start, loop end, pointer decrement, pointer increment, cell increment, cell decrement
bf_commands = [".", ",", "[", "]", "<", ">", "+", "-"]
executor_commands = ["OUT", "IN", "LS", "LE", "PI", "PD", "CI", "CD"]
audio_commands = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000]

python_startcode = 12345
executor_startcode = 1213

class Translator:
    def __init__(self):
        self.audio_commands = audio_commands
        self.executor_commands = executor_commands

    def _translate(self, data, from_commands, to_commands):
        out = []
        for command in data:
            if command not in from_commands:
                continue
            from_index = from_commands.index(command)
            to_command = to_commands[from_index]
            out.append(to_command)

        return out

    def python_to_audio(self, python):
        out = [python_startcode]
        for char in python:
            out.append(ord(char))
        return out


    def audio_to_python(self, audio: list):
        if audio[0] == python_startcode:
            del audio[0]
        code = "".join([chr(x) for x in audio])
        return code

    def bf_to_executor(self, bf_data):
        return [executor_startcode] + self._translate(bf_data, bf_commands, executor_commands)

    def executor_to_bf(self, executor_data):
        if executor_data[0] == executor_startcode:
            del executor_data[0]
        return self._translate(executor_data, executor_commands, bf_commands)

    def executor_to_audio(self, executor_data: list):
        if executor_data[0] == executor_startcode:
            del executor_data[0]
        return self._translate(executor_data, self.executor_commands, self.audio_commands)

    def audio_to_executor(self, audio_data: list):
        return [executor_startcode] + self._translate(audio_data, self.audio_commands, self.executor_commands)

    def text_to_executor(self, text: str) -> list:
        out = []
        pointer = 0

        for char in text:
            c = ord(char)
            difference = c-pointer
            if difference > 0:
                out+=([self.executor_commands[6]]*abs(difference))
            elif difference < 0:
                out+=([self.executor_commands[7]] * abs(difference))

            pointer+=difference

            out.append(self.executor_commands[0])

        return out