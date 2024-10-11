import pyaudio
import wave
from pydub import AudioSegment

def mp3_to_wav(mp3_filename, wav_filename=None):
    # Load your mp3 file
    audio = AudioSegment.from_mp3(mp3_filename)
    
    # Set the output wav filename if not provided
    if not wav_filename:
        wav_filename = mp3_filename.replace(".mp3", ".wav")
    
    # Export the audio to wav format
    audio.export(wav_filename, format="wav")
    print(f"Conversion complete: {wav_filename}")

def record_to_wav(RECORD_SECONDS, WAVE_OUTPUT_FILENAME):
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100


    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("* recording")

    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("* done recording")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

