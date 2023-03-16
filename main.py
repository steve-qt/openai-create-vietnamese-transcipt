# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import openai
import binascii


def create_transcription():
  openai.api_key = ""
  audio_file = open("hi-vietnam.mp3", "rb")
  transcript = openai.Audio.transcribe("whisper-1", audio_file)
  a = binascii.hexlify(transcript.text.encode('cp1258', errors='backslashreplace'))
  print(binascii.unhexlify(a).decode('unicode-escape'))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    create_transcription()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
