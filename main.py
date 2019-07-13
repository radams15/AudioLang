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

    audio_file.write(audio_data)

def write_bf(bf_code, file):
    code = t.bf_to_executor(bf_code)
    write_executable_code(code, file)

def write_python(code, file):
    audio_file = audio.Audio(file)
    audio_data = t.python_to_audio(code)
    audio_file.write(audio_data)

def execute_file(file):
    audio_file = audio.Audio(file)
    e = executor.Executor()

    audio_data = audio_file.read()
    if audio_data[0] == translator.python_startcode:
        python_code = t.audio_to_python(audio_data)

        for i in range(len(argv)):
            if argv[i] == file:
                del argv[i]

        exec(python_code)
    elif audio_data[0] == translator.executor_startcode:
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

    try:
        if argv[1] == "-e":
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

        elif argv[1] == "-ep":
            python = argv[2]
            out_file = argv[3]
            write_python(python, out_file)

        elif argv[1] == "-epf":
            python_file = argv[2]
            if not path.exists(python_file):
                print("No Such File")
            else:
                python = open(python_file, "r").read()
                out_file = argv[3]
                write_python(python, out_file)

        elif len(argv) == 2:
            if path.exists(argv[1]):
                execute_file(argv[1])
            else:
                print("No Such File")

        else:
            print(help_message)
    except IndexError:
        print(help_message)