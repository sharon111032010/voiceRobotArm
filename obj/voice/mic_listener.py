import queue
import sounddevice as sd


class MicListener:

    def __init__(
        self,
        samplerate=16000,
        blocksize=1280
    ):

        self.queue = queue.Queue()

        self.stream = sd.InputStream(
            samplerate=samplerate,
            channels=1,
            dtype="float32",
            blocksize=blocksize,
            callback=self.callback
        )


    def callback(self, indata, frames, time, status):

        # print("callback", indata.shape)
        if status:
            print(status)

        self.queue.put(
            indata.copy()
        )


    def start(self):

        self.stream.start()
        print("MIC 開啟")


    def read(self):

        return self.queue.get()


    def stop(self):

        self.stream.stop()
        self.stream.close()
        
    def clear(self):
        while not self.queue.empty():
            try:
                self.queue.get_nowait()
            except queue.Empty:
                break
            