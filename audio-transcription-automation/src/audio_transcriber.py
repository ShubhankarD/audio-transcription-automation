import whisper
from pydub import AudioSegment
import os
import math
import multiprocessing

def load_audio(audio_path):
    return AudioSegment.from_file(audio_path)

def split_audio(audio, chunk_length_ms):
    chunks = []
    for i in range(0, len(audio), chunk_length_ms):
        chunks.append(audio[i:i + chunk_length_ms])
    return chunks

def transcribe_chunk(model, chunk):
    return model.transcribe(chunk)

def combine_transcriptions(transcriptions):
    return " ".join(transcriptions)

def main(audio_path, chunk_length_ms, language):
    model = whisper.load_model("base")
    audio = load_audio(audio_path)
    chunks = split_audio(audio, chunk_length_ms)

    with multiprocessing.Pool() as pool:
        transcriptions = pool.map(lambda chunk: transcribe_chunk(model, chunk), chunks)

    combined_transcription = combine_transcriptions(transcriptions)
    
    output_file = "transcription_output.txt"
    with open(output_file, "w") as f:
        f.write(combined_transcription)

if __name__ == "__main__":
    audio_path = "/path/to/your/audio/file.mp3"  # Update this path
    chunk_length_ms = 60 * 1000  # 60 seconds
    language = "en"  # Update this language if needed
    main(audio_path, chunk_length_ms, language)