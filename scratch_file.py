#%%
from src.audio_utils import record_to_wav, mp3_to_wav
from models.whisper import whisper_inference
import time


# %%
if __name__ == '__main__':
    # RECORD_SECONDS = 10
    # WAVE_OUTPUT_FILENAME = "voice.wav"
    # record_to_wav(RECORD_SECONDS, WAVE_OUTPUT_FILENAME)

    wav_file_name = "test.wav"
    mp3_file_name = "Lex_Sam_1Hour.mp3"
    mp3_to_wav(mp3_file_name, wav_file_name)


    start_time = time.time()

    file_name = wav_file_name
    model_name = "base"

    result = whisper_inference(file_name, model_name)
    print("result", result)

    end_time = time.time()

    elapsed_time = end_time - start_time
    print("elapsed_time", elapsed_time)

    

# %%
