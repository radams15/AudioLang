import audio
import executor


class Translator:
    def __init__(self):
        self.audio_commands = audio.Audio(None).commands
        self.executor_commands = executor.Executor().commands
        self.

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
        out = []
        for command in executor_data:
            if command not in self.executor_commands:
                continue
            executor_index = self.executor_commands.index(command)
            audio_command = self.audio_commands[executor_index]
            out.append(audio_command)

        return out

    def audio_to_executor(self, audio_data: list):
        out = []
        for command in audio_data:
            audio_index = self.audio_commands.index(command)
            executor_command = self.executor_commands[audio_index]
            out.append(executor_command)

        return out