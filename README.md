# Audio Transcription Automation

This project automates audio transcription using the Whisper ASR model. It splits a large audio file into smaller chunks, transcribes each chunk using multiprocessing, and combines the results into a single output file.

## Requirements

- Python 3.6+
- [Whisper](https://github.com/openai/whisper)
- pydub
- ffmpeg (required by pydub)

## Installation

1.  Install the required Python packages:

    ```bash
    pip install whisper pydub
    ```

2.  Ensure that `ffmpeg` is installed and available in your system's PATH.

    -   For macOS, you can install it using Homebrew:

        ```bash
        brew install ffmpeg
        ```

    -   For Debian-based Linux distributions:

        ```bash
        sudo apt update
        sudo apt install ffmpeg
        ```

## Usage

1.  Modify the script's configuration section:

    -   `audio_path`: Path to the input audio file.
    -   `chunk_length_ms`: Length of each audio chunk in milliseconds.
    -   `language`: Language of the audio.

2.  Run the script:

    ```bash
    python "Whishper Automation.py"
    ```

3.  The transcribed text will be saved to `transcription_output.txt`.

## Configuration

```python
audio_path = "/Users/sdash029/Downloads/test audio.mp3"  # Path to the input audio file
chunk_length_ms = 60 * 1000  # Length of each audio chunk in milliseconds (default: 60 seconds)
language = "hi"  # Language of the audio
```
