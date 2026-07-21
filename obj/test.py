from voice.mic_listener import MicListener
from voice.vad_listener import VADListener
from voice.whisper_recognizer import WhisperRecognizer

from command.parser import CommandParser
from robot.niryo_robot import NiryoRobot
from voice.wake_word import WakeWordDetector

import time

mic = MicListener()

vad = VADListener()

whisper = WhisperRecognizer()

wake = WakeWordDetector()

parser = CommandParser()

robot = NiryoRobot()


mic.start()


awake = False


while True:

    audio = mic.read()


    # ======================
    # 等待喚醒詞
    # ======================
    if not awake:

        if wake.detect(audio):

            print("已喚醒")

            mic.clear()

            awake = True

            for _ in range(3):
                mic.read()

            vad.reset()

        continue



    # ======================
    # 已喚醒，等待指令
    # ======================

    sentence = vad.process(
        audio
    )


    if sentence is not None:


        print("收到語音")


        text = whisper.transcribe_audio(
            sentence
        )


        print(
            "辨識:",
            text
        )


        command = parser.parse(
            text
        )


        if command:

            print(
                "命令:",
                command
            )


            # start,end = command
            # robot.grab(start,end)


        # 完成一次指令
        awake = False
        mic.clear()