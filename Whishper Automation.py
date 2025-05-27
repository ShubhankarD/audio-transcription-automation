import whisper
from multiprocessing import Pool, cpu_count
from pydub import AudioSegment
import os

# Config
audio_path = "/Users/sdash029/Downloads/test audio.mp3"
chunk_length_ms = 60 * 1000  # 60 seconds
language = "hi"

# Load full audio
audio = AudioSegment.from_file(audio_path)
duration_ms = len(audio)

# Split audio into chunks
chunks = [
    audio[i:i + chunk_length_ms]
    for i in range(0, duration_ms, chunk_length_ms)
]

# Save chunks to temp folder
chunk_paths = []
os.makedirs("chunks", exist_ok=True)
for idx, chunk in enumerate(chunks):
    path = f"chunks/chunk_{idx}.mp3"
    chunk.export(path, format="mp3")
    chunk_paths.append((path, idx))  # include index to preserve order

# Transcribe chunk
def transcribe_chunk(args):
    path, idx = args
    model = whisper.load_model("medium")  # load inside subprocess
    result = model.transcribe(path, language=language)
    return (idx, result["text"])

# Run multiprocessing
if __name__ == "__main__":
    with Pool(cpu_count()) as pool:
        results = pool.map(transcribe_chunk, chunk_paths)

    # Sort by original order
    results.sort(key=lambda x: x[0])

    # Combine and save output
    with open("transcription_output.txt", "w", encoding="utf-8") as f:
        for _, text in results:
            f.write(text + "\n\n")

    print("✅ Transcription complete. Output saved to transcription_output.txt.")
