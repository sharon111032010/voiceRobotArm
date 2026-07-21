import whisper

class WhisperRecognizer:

    def __init__(self, model_name="base"):
        self.model = whisper.load_model(model_name)

    # 讀取檔案轉文字
    def transcribe(self, file_path):

        result = self.model.transcribe(
            file_path,
            language="zh",
            fp16=False
        )

        return result["text"]
    #  讀取音訊轉文字
    def transcribe_audio(self, audio):
        result = self.model.transcribe(
            audio,
            language="zh",
            fp16=False,
            temperature=0,
            condition_on_previous_text=False
        )
        return result["text"]