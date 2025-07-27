from gtts import gTTS
import os

def convert_text_to_mp3(text, output_path="output.mp3"):
    """
    Converts the given text into an MP3 audio file.

    Args:
        text (str): The text to convert into speech.
        output_path (str): The path to save the output MP3 file.
    """
    if not text.strip():
        print("Error: Input text cannot be empty.")
        return

    try:
        tts = gTTS(text=text, lang='en')
        tts.save(output_path)
        print(f"Successfully converted text to {output_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    sample_text = "The heir, whose hair is fair, can't bear to tear the rare pear there; instead, they're going to pare it. Peter Piper picked a peck of pickled peppers. She sells seashells by the seashore. The sixth sick sheik's sixth sheep's sick."
    output_file = "data/hard_to_transcribe.mp3"
    convert_text_to_mp3(sample_text, output_path=output_file)