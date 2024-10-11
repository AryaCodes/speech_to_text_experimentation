import whisper


def whisper_inference(file_name, model_name = "base"):
        model = whisper.load_model(model_name)
        result = model.transcribe(file_name)
        
        output_text = result["text"]
        return output_text