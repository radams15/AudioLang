import wave

commands = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000]

class Audio:
    def __init__(self, file):
        self.file = file
        self.commands = commands

    def read(self):
        out_raw = ""
        with wave.open(self.file, 'rb') as w:
            for i in range(w.getnframes()):
                frame = w.readframes(1)

                f1 = frame.decode()

                out_raw+=f1

        out=[]
        for byte in out_raw.split("0x"):
            if not byte: continue
            out.append(int(byte, 16))

        return out

    def write(self, data):
        with wave.open(self.file, 'wb') as w:
            w.setnchannels(1)
            w.setsampwidth(1)
            w.setframerate(8000)
            w.setnframes(len(data))

            for d in data:
                encoded = hex(d).encode()
                w.writeframes(encoded)
