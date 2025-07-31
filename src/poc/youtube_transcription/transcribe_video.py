from faster_whisper import WhisperModel
import os

def transcribe_audio(audio_path, output_file):
    model_size = "large-v2"

    # Initialize the Whisper model
    model = WhisperModel(model_size, device="cpu", compute_type="int8")

    # Transcribe the audio file
    segments, info = model.transcribe(audio_path, beam_size=5)

    #transcript = " ".join([segment.text for segment in segments])

    print(f"Detected language '{info.language}' with probability {info.language_probability}")

    # Open the output file and write the transcribed text
    with open(output_file, "w") as f:
        for segment in segments:
            f.write(segment.text + "\n")

    print(f"Transcription complete. Output saved to {output_file}")

if __name__ == '__main__':
    audio_file_name = 'hard_to_transcribe'
    audio_type = 'mp3'
    audio_to_transcribe = f"/home/yash/code/StockPredictor/data/{audio_file_name}.{audio_type}"
    #audio_to_transcribe = "/home/yash/code/StockPredictor/data/hard_to_transcribe.mp3"
    output_filename = f"/home/yash/code/StockPredictor/data/transcribed_text/{audio_file_name}.txt"
    
    transcribe_audio(audio_to_transcribe, output_filename)