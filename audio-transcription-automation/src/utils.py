def split_audio_into_chunks(audio_path, chunk_length_ms):
    from pydub import AudioSegment
    audio = AudioSegment.from_file(audio_path)
    chunks = []
    
    for i in range(0, len(audio), chunk_length_ms):
        chunk = audio[i:i + chunk_length_ms]
        chunks.append(chunk)
    
    return chunks

def save_chunks_to_files(chunks, output_dir):
    import os
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    file_paths = []
    for i, chunk in enumerate(chunks):
        chunk_file_path = os.path.join(output_dir, f"chunk_{i}.wav")
        chunk.export(chunk_file_path, format="wav")
        file_paths.append(chunk_file_path)
    
    return file_paths

def load_audio_file(audio_path):
    from pydub import AudioSegment
    return AudioSegment.from_file(audio_path)