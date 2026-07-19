import whisper


class WhisperRecognizer:

    def __init__(self, model_name="base"):
        self.model = whisper.load_model(model_name)


    def transcribe(self, file_path):

        result = self.model.transcribe(
            file_path,
            language="zh",
            fp16=False
        )

        return result["text"]