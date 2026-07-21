from voice.mic_listener import MicListener
from voice.vad_listener import VADListener
from voice.whisper_recognizer import WhisperRecognizer

from command.parser import CommandParser
from robot.niryo_robot import NiryoRobot
from voice.wake_word import WakeWordDetector


mic = MicListener()

vad = VADListener()

whisper = WhisperRecognizer()

wake = WakeWordDetector()

parser = CommandParser()

robot = NiryoRobot()



mic.start()


while True:

    audio = mic.read()
    #print(type(audio), getattr(audio, "shape", None))
    # print(audio.shape)
    # print(audio.dtype)
    # 等待喚醒詞
    # print(audio.shape, audio.dtype)
    if not wake.detect(audio):
        continue

    print(
        "已喚醒"
    )

    # 開始等待指令
    sentence = vad.process(
        audio
    )

    if sentence:

        text = whisper.transcribe_audio(
            sentence
        )
    
        command = parser.parse(
            text
        )

        # if command:

        #     start,end = command

        #     robot.grab(
        #         start,
        #         end
        #     )