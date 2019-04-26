import translator
import audio
import executor

if __name__ == '__main__':
    d1=">++++++++[-<+++++++++>]<.>>+>-[+]++>++>+++[>[->+++<<+++>]<<]>-----.>->+++..+++.>-.<<+[>[+>+]>>]<--------------.>>.+++.------.--------.>+.>+."
    audio = audio.Audio("hello_world.wav")

    t = translator.Translator()
    audio_data = t.executor_to_audio(list(d1))

    audio.write(audio_data)

    audio_data = audio.read()

    print(audio_data)
