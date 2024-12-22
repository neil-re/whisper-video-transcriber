import whisper
import ffmpeg
import os
import time

"""
This script reads a video file path from 'path_video.txt',
converts the video to audio using ffmpeg, then uses the
OpenAI Whisper model to transcribe the audio into text
and generates an SRT subtitle file.
"""

# Load the Whisper model
model = whisper.load_model("base")

def convert_video_to_audio(video_path: str) -> str:
    """
    Converts a video file to an MP3 audio file using ffmpeg.

    :param video_path: The absolute or relative path to the video file.
    :return: The path to the generated MP3 file, or None if conversion fails.
    """
    audio_output = os.path.splitext(video_path)[0] + '.mp3'

    try:
        ffmpeg.input(video_path).output(audio_output).run()
        print(f"Audio extracted: {audio_output}")
    except ffmpeg.Error as e:
        print(f"Error converting video to audio: {str(e)}")
        return None
    
    return audio_output

def format_timestamp(seconds: float) -> str:
    """
    Formats a floating-point timestamp into SRT-compatible string: HH:MM:SS,mmm

    :param seconds: Timestamp in seconds (can include decimals).
    :return: A string in the format 'HH:MM:SS,mmm'
    """
    milliseconds = int((seconds - int(seconds)) * 1000)
    timestamp = time.strftime('%H:%M:%S', time.gmtime(seconds))
    return f"{timestamp},{milliseconds:03d}"

def write_srt(segments: list, filename: str) -> None:
    """
    Writes segments of transcribed text into an SRT file.

    :param segments: A list of segment dictionaries, usually from whisper.transcribe().
    :param filename: Path to the output SRT file.
    """
    with open(filename, 'w', encoding='utf-8') as srt_file:
        for i, segment in enumerate(segments):
            srt_file.write(f"{i + 1}\n")
            start = format_timestamp(segment['start'])
            end = format_timestamp(segment['end'])
            srt_file.write(f"{start} --> {end}\n")
            srt_file.write(f"{segment['text'].strip()}\n\n")

def transcribe_audio(audio_path: str) -> None:
    """
    Transcribes the given audio file using Whisper and
    generates both a .txt file for the transcript and
    a .srt file for subtitles.

    :param audio_path: The path to the audio file (e.g., .mp3).
    """
    result = model.transcribe(audio_path)
    transcribed_text = result['text']
    
    print("Full transcription:")
    print(transcribed_text)
    
    txt_output = os.path.splitext(audio_path)[0] + '.txt'
    with open(txt_output, 'w', encoding='utf-8') as txt_file:
        txt_file.write(transcribed_text)
    
    print(f"Transcription saved to: {txt_output}")

    srt_output = os.path.splitext(audio_path)[0] + '.srt'
    write_srt(result['segments'], srt_output)
    print(f"Subtitles saved to: {srt_output}")

def read_video_path() -> str:
    """
    Reads the video path from 'path_video.txt'.

    :return: The path to the video file, or None if the file cannot be found.
    """
    file_name = 'path_video.txt'
    if os.path.exists(file_name):
        with open(file_name, 'r', encoding='utf-8') as f:
            return f.read().strip()
    else:
        print(f"File not found: {file_name}")
        return None

def main():
    video_path = read_video_path()
    if not video_path:
        print("No video path available. Please check 'path_video.txt'.")
        return

    audio_path = convert_video_to_audio(video_path)
    if audio_path:
        transcribe_audio(audio_path)
        # If you do not want to keep the audio file, uncomment the line below:
        # os.remove(audio_path)

if __name__ == "__main__":
    main()
