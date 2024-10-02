# Autosubtitle Tool

This tool uses OpenAI's Whisper model to transcribe videos into text. It automatically creates a virtual environment, installs dependencies, and transcribes the specified video using Whisper.

## Features
- Automatically sets up a virtual environment.
- Installs necessary dependencies (if not already installed).
- Uses OpenAI's Whisper model for transcription.
- Takes video file paths as input through a single command.

## Prerequisites
- Python 3.8 or newer installed on your system.
- `ffmpeg` installed and available in your system's PATH.
  - On macOS, you can install `ffmpeg` using Homebrew:
    ```bash
    brew install ffmpeg
    ```

## How to Use
   ```
   git clone https://github.com/egeozsoy/autosubtitle.git  
   cd autosubtitle
   chmod +x autosubtitle.sh
   ./autosubtitle.sh /path/to/your/video.mp4
   ```
   
   The subtitle will be exported next to your video.



