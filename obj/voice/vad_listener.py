import torch
import numpy as np
from silero_vad import load_silero_vad


class VADListener:

    def __init__(self):

        self.model = load_silero_vad()

        self.buffer = []

        self.speaking = False

        self.silence = 0

        # Silero VAD 16kHz 固定 512 samples
        self.chunk_size = 512


    def process(self, audio):

        # 確保 float32
        audio = audio.flatten().astype(np.float32)


        result = None


        # 切成 Silero 支援的大小
        for i in range(0, len(audio), self.chunk_size):

            chunk = audio[i:i+self.chunk_size]


            # 不足512丟掉
            if len(chunk) != self.chunk_size:
                continue


            tensor = torch.from_numpy(chunk)


            speech = self.model(
                tensor,
                16000
            ).item()



            # 有聲音
            if speech > 0.5:

                self.buffer.append(chunk.copy())

                self.speaking = True

                self.silence = 0



            # 靜音
            else:

                if self.speaking:

                    self.silence += 1


                    # 5個512 frame
                    # 512 / 16000 = 32ms
                    # 5次約160ms
                    if self.silence > 25:


                        result = np.concatenate(
                            self.buffer
                        )


                        self.buffer.clear()

                        self.speaking = False

                        self.silence = 0


                        return result



        return None