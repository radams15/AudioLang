from audio import Audio

#out, in, loop start, loop end, pointer decrement, pointer increment, cell increment, cell decrement
bf_commands = [".", ",", "[", "]", "<", ">", "+", "-"]
executor_commands = [bin(ord(b)) for b in bf_commands]
audio_commands = [1145, 5246, 7431, 6659, 5897, 3768, 3479, 7461] #[int(b, 2)*2 for b in executor_commands]

#executor_commands = bf_commands
#audio_commands = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000]

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

    def bf_to_executor(self, bf_data):
        return self._translate(bf_data, bf_commands, executor_commands)

    def executor_to_bf(self, executor_data):
        return self._translate(executor_data, executor_commands, bf_commands)

    def executor_to_audio(self, executor_data: list):
        return self._translate(executor_data, self.executor_commands, self.audio_commands)

    def audio_to_executor(self, audio_data: list):
        return self._translate(audio_data, self.audio_commands, self.executor_commands)

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