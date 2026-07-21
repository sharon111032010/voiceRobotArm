import queue
import sounddevice as sd
import numpy as np


class MicListener:
    def __init__(
        self,
        samplerate=16000,
        channels=1,
        blocksize=1024
    ):
        self.samplerate = samplerate
        self.channels = channels
        self.blocksize = blocksize

        self.audio_queue = queue.Queue()

        self.stream = sd.InputStream(
            samplerate=self.samplerate,
            channels=self.channels,
            dtype="float32",
            blocksize=self.blocksize,
            callback=self._callback
        )

    def _callback(self, indata, frames, time, status):
        if status:
            print(status)

        # 存一份，避免 buffer 被覆寫
        self.audio_queue.put(indata.copy())

    def start(self):
        self.stream.start()
        print("🎤 Mic Started")

    def stop(self):
        self.stream.stop()
        self.stream.close()
        print("🎤 Mic Stopped")

    def listen(self, seconds=3):
        """
        收集指定秒數音訊
        回傳 numpy.ndarray(float32)
        """

        blocks = []

        total_frames = int(seconds * self.samplerate)
        current_frames = 0

        while current_frames < total_frames:

            data = self.audio_queue.get()

            blocks.append(data)

            current_frames += len(data)

        audio = np.concatenate(blocks, axis=0)

        return audio.flatten()