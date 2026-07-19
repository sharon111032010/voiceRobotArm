import whisper

def transcribe_mp3(file_path):
    # 載入模型（第一次會自動下載）
    model = whisper.load_model("base")

    # 辨識中文
    result = model.transcribe(
        file_path,
        language="zh",
        fp16=False  # Windows 沒有 CUDA 時建議加上
    )

    return result["text"]


if __name__ == "__main__":
    file_path = "record.mp3"

    text = transcribe_mp3(file_path)

    print("辨識結果：")
    print(text)
