import translator
import audio
import executor

t = translator.Translator()

def write_executable_code(code, file):
    audio_file = audio.Audio(file)

    audio_data = t.executor_to_audio(list(code))
    audio_file.write(audio_data)

def execute_file(file):
    audio_file = audio.Audio(file)
    e = executor.Executor()

    audio_data = audio_file.read()
    executable_data = t.audio_to_executor(audio_data)

    e.execute(executable_data)


if __name__ == '__main__':
    #calculator = "+>+>+>+>>>,.>++++[<---------->-]<-------[-<[>>+<<-]>>[<<++++++++++>>-]<[<+>-],.>++++[<---------->-]<--[>+<-]>[<<<<<<<->>>>>>>-[<<<<<<->>>>>>--[<<<<<->>>>>--[<<<<<<<+>+>+>>>>>[<+>-]]]]]<]>,.>++++[<---------->-]<-------[-<[>>+<<-]>>[<<++++++++++>>-]<[<+>-],.>++++[<---------->-]<-------[>+>+<<-]>>[<<+>>-]<-[-[-[-[-[-[-[-[-[-[<[-]>[-]]]]]]]]]]]<]<<<<<<<[->->->->>[>>+<<-]>[>[<<+>>>+<-]>[<+>-]<<-]>[-]<<<<<<<]>[->->->>>[<+>-]<<<<<]>[->->+>>[>+<-]>>+<[>-<[<+>-]]>[-<<<<->[>+<-]>>>]<<<[->-[>+<-]>>+<[>-<[<+>-]]>[-<<<<->[>+<-]>>>]<<<]>[<+>-]<<<<]>[->>>>>+[-<<<[>>>+>+<<<<-]>>>[<<<+>>>-]<<[>>+>>+<<<<-]>>[<<+>>-]>[->->>+<<[>+<-]>[>-<[<+>-]]>[-<<<<+<+<<[-]>>>>[<<<<+>>>>-]>>>]<<<]>[-]<<]<<[-]<[>+<-]>>[<<+>>-]<<<<]>>>[>>+[<<[>>>+>+<<<<-]>>>>[<<<<+>>>>-]+<[-[-[-[-[-[-[-[-[-[>-<<<<---------->+>>[-]]]]]]]]]]]>[->[>]>++++[<++++++++++>-]<++++++++[<]<<<<[>>>>>[>]<+[<]<<<<-]>>-<[>+<[<+>-]]>>>]<<]>>>[>]>++++[<++++++++++>-]<++++++>>++++[<++++++++++>-]<++++++>>++++[<++++++++++>-]<++++++[<]<<<<]>+[<<[>>>+>+<<<<-]>>>>[<<<<+>>>>-]+<[-[-[-[-[-[-[-[-[-[>-<<<<---------->+>>[-]]]]]]]]]]]>[->>[>]>++++[<++++++++++>-]<++++++++[<]<<<<<[>>>>>>[>]<+[<]<<<<<-]>>-<[>+<[<+>-]]>>>]<<]<<<[->>>>>>>[>]>++++[<++++++++++>-]<+++++[<]<<<<<<]>>>>>>>[>]<[.<]"
    #write_executable_code(calculator, "calc.wav")
    #execute_file("calc.wav")

    #text = t.text_to_executor(open("text.txt", "r").read())
    #write_executable_code(text, "text.wav")
    execute_file("text.wav")