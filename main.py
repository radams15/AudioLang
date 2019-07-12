#!/usr/bin/env python3

from sys import argv
import os.path as path

import translator
import audio
import executor

t = translator.Translator()

def write_executable_code(code, file):
    audio_file = audio.Audio(file)

    audio_data = t.executor_to_audio(list(code))

    audio_file.write_executor(audio_data)

def write_bf(bf_code, file):
    code = t.bf_to_executor(bf_code)
    write_executable_code(code, file)

def execute_file(file):
    audio_file = audio.Audio(file)
    e = executor.Executor()

    audio_data = audio_file.read()
    executable_data = t.audio_to_executor(audio_data)

    e.execute(executable_data)

help_message = """\
AudioLang!

Usage:
    -e  [CODE] [OUT_FILE]     Write Pure Executor Script
    -eb [CODE] [OUT FILE]     Write Brainf*ck Script
    -et [TEXT] [OUT FILE]     Write Executor Script To Output Text
    (No Args)   [IN FILE]     Execute File
"""


if __name__ == '__main__':
    if len(argv) < 2:
        print(help_message)

    elif argv[1] == "-e":
        code = argv[2]
        out_file = argv[3]
        write_executable_code(code, out_file)

    elif argv[1] == "-eb":
        code = argv[2]
        out_file = argv[3]
        write_bf(code, out_file)

    elif argv[1] == "-et":
        text = argv[2]
        out_file = argv[3]
        executor_text = t.text_to_executor(text)
        write_executable_code(executor_text, out_file)

    elif len(argv) == 2:
        if path.exists(argv[1]):
            execute_file(argv[1])