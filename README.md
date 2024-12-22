# Whisper Video Transcriber

A Python script that:
1. Reads the path of a video file from `path_video.txt`.
2. Converts the video to an audio file (`.mp3`) using FFmpeg.
3. Uses [OpenAI Whisper](https://github.com/openai/whisper) to:
   - Transcribe the audio into a `.txt` file.
   - Generate `.srt` subtitles with timestamps.

## Features

- Automatic audio extraction from video (`.mp4`, `.mov`, etc.).
- Option to remove the generated audio file after processing.
- Simple text-based configuration via `path_video.txt`.

## Requirements

- Python 3.7 or above  
- [PyTorch](https://pytorch.org)  
- [OpenAI Whisper](https://github.com/openai/whisper)  
- [FFmpeg](https://ffmpeg.org) installed on your system  
- `ffmpeg-python`  

You can install dependencies using:

```bash
pip install -r requirements.txt
