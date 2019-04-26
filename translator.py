import audio
import executor


class Translator:
    def __init__(self):
        self.audio_commands = audio.Audio(None).commands
        self.executor_commands = executor.Executor().commands

    def executor_to_audio(self, executor_data: list):
        out = []
        for command in executor_data:
            executor_index = self.executor_commands.index(command)
            audio_command = self.audio_commands[executor_index]
            out.append(audio_command)

        return out

    def audio_to_executor(self, audio_data: list):
        out = []
        for command in audio_data:
            audio_index = self.audio_commands.index(command)
            executor_command = self.audio_commands[audio_index]
            out.append(executor_command)

        return out
