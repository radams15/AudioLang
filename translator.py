import audio
import executor

import os


class Translator:
    def __init__(self):
        self.audio_commands = audio.Audio(None).commands
        self.executor_commands = executor.Executor().commands

    def _translate(self, data, from_commands, to_commands):
        out = []
        for command in data:
            if command not in from_commands:
                continue
            from_index = from_commands.index(command)
            to_command = to_commands[from_index]
            out.append(to_command)

        return out


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