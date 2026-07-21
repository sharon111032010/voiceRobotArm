import openwakeword
from openwakeword.model import Model
import numpy as np
import time

class WakeWordDetector:

    def __init__(self):
        self.model = Model(
            inference_framework="onnx"
        )
        self.last_trigger = 0

        print(
            "目前喚醒詞:",
            self.model.models.keys()
        )


    def detect(self, audio):

        # (512,1) -> (512,)
        audio = audio.flatten()

        # float32 (-1~1) -> int16 PCM
        audio = (audio * 32767).astype(np.int16)

        result = self.model.predict(
            audio
        )

        print("jarvis:",result["hey_jarvis"])   

        for key, value in result.items():

            if value > 0.75:

                now = time.time()

                if now - self.last_trigger < 2:

                    return False
                
                print("Wake word:", key,value)

                self.last_trigger = now
                
                return True
            
        return False