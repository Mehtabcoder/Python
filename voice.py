from gtts import gTTS
import platform
import subprocess
import os

def play_audio(file_path):
    system = platform.system()
    try:
        if system == "Windows":
            os.startfile(file_path)
        elif system == "Darwin":
            subprocess.call(["afplay", file_path])
        elif system == "Linux":
            subprocess.call(["xdg-open", file_path])
        else:
            print("Unsupported OS for audio playback.")
    except Exception as e:
        print(f"Error playing audio: {e}")

def text_to_speech(text, lang='en', filename="output.mp3"):
    try:
        tts = gTTS(text=text, lang=lang)
        tts.save(filename)
        print(f"Audio saved as {filename}")
        play_audio(filename)
    except Exception as e:
        print(f"Text-to-speech failed: {e}")

if __name__ == "__main__":
    text = "Hello! This is a sample text to convert to speech."
    text_to_speech(text)
