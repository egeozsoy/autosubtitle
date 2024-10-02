from pathlib import Path
import argparse
import whisper
from whisper.utils import get_writer

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Automatically create subtitles for a video using Whisper.")
    parser.add_argument('video_path', type=str, help='Path to the video file to process.')
    args = parser.parse_args()
    
    VIDEO_PATH = Path(args.video_path)
    
    if not VIDEO_PATH.exists():
        print(f"Error: The specified video file '{VIDEO_PATH}' does not exist.")
        sys.exit(1)

    export_transcript_path = VIDEO_PATH.parent / f'{VIDEO_PATH.stem}.srt'

    model = whisper.load_model("turbo")
    print(f'Processing {VIDEO_PATH}')
    result = model.transcribe(str(VIDEO_PATH), language="en", task="transcribe", condition_on_previous_text=False, verbose=False)
    
    writer = get_writer('srt', str(export_transcript_path.parent))
    writer(result, str(export_transcript_path))
    print(f'Transcription completed and saved to {export_transcript_path}')

if __name__ == '__main__':
    main()