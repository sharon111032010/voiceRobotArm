
from voice.whisper_recognizer import WhisperRecognizer
from command.parser import CommandParser
from robot.niryo_robot import NiryoController


from pathlib import Path




def main():


    # 語音物件
    voice = WhisperRecognizer()


    # 解析物件
    parser = CommandParser()


    # 機械手臂物件
    robot = NiryoController(
        "192.168.0.4"
    )


    try:


        # 1. 語音辨識

        text = voice.transcribe(
            "record.mp3"
        )

        BASE_DIR = Path(__file__).parent

        # audio_file = BASE_DIR /"mp3"/ "record.mp3"
        audio_file = BASE_DIR /"mp3"/ "6-5.mp3"


        text = voice.transcribe(
            str(audio_file)
        )


        print(
            "辨識:",
            text
        )



        # 2. 解析

        command = parser.parse(
            text
        )


        if command:


            start,end = command


            print(
                f"收到命令 {start}->{end}"
            )


            # 3. 控制機械手

            robot.home()

            robot.move_block(
                start,
                end
            )

            robot.home()



        else:

            print(
                "無法理解指令"
            )



    finally:

        robot.close()



if __name__=="__main__":

    main()