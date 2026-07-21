import torch
import numpy as np
from silero_vad import load_silero_vad


class VADListener:


    def __init__(self):

        self.model = load_silero_vad()

        self.buffer = []

        self.speaking = False

        self.silence = 0



    def process(self, audio):

        audio = torch.from_numpy(
            audio.flatten()
        )


        speech = self.model(
            audio,
            16000
        ).item()


        # 有講話
        if speech > 0.5:

            self.buffer.append(
                audio.numpy()
            )

            self.speaking = True
            self.silence = 0


        # 沒講話
        else:

            if self.speaking:

                self.silence += 1


                # 約0.8秒沒聲音
                if self.silence > 5:

                    result = np.concatenate(
                        self.buffer
                    )


                    self.buffer.clear()

                    self.speaking = False
                    self.silence = 0


                    return result


        return None
    