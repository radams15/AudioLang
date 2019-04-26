import translator
import audio
import executor

def write_executable_code(code, file):
    t = translator.Translator()
    audio_file = audio.Audio(file)

    audio_data = t.executor_to_audio(list(code))
    audio_file.write(audio_data)

def execute_file(file):
    audio_file = audio.Audio(file)
    t = translator.Translator()
    e = executor.Executor()

    audio_data = audio_file.read()
    executable_data = t.audio_to_executor(audio_data)

    e.execute(executable_data)

if __name__ == '__main__':
    #write_executable_code(d2, "calc.wav")
    execute_file("calc.wav")
