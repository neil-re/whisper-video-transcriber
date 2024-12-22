# Whisper Video Transcriber

Script en Python que extrae audio de un archivo de video con FFmpeg, lo transcribe usando el modelo Whisper de OpenAI y genera tanto un archivo de texto como un archivo de subtítulos `.srt`.

## Características
- Convierte automáticamente videos a archivos de audio `.mp3`.
- Utiliza el modelo `base` de Whisper para transcribir audio a texto.
- Genera subtítulos en formato `.srt` con marcas de tiempo.
- Lee la ruta del video desde un archivo de texto (`ruta_video.txt`) para evitar modificar el script.

## Tecnologías / Dependencias
- Python 3.7+
- [PyTorch](https://pytorch.org/) 
- [Whisper de OpenAI](https://github.com/openai/whisper) 
- [FFmpeg](https://ffmpeg.org/)
- `ffmpeg-python`

## Uso rápido
1. Clona el repositorio.
2. Crea y activa un entorno virtual (opcional).
3. `pip install -r requirements.txt`
4. Coloca la ruta de tu video en `ruta_video.txt`.
5. Ejecuta `python main.py` para generar la transcripción y subtítulos.
