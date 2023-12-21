"""
The Text to speech code implementation in OCR shall be used in in this feature too
"""

import  pyttsx3
import json, logging as log
log.basicConfig(level=log.INFO)

class text_to_speech_engine():
    def __init__(self, text_path, rate):
        self.text_path = text_path
        self.rate = rate

    def TTS(self):
        with open(self.text_path, "r+") as to_read:
            to_read.seek(0)
            read = to_read.read()
            engine = pyttsx3.init()
            engine.setProperty('rate', self.rate)
            log.info(read)
            log.info(engine.getProperty('rate'))
            engine.say(read)
            engine.runAndWait()
            engine.stop()
    
def main():
    text_path = "D:/vizuosense_mine/STT/Resources/text_file.txt"
    rate = 150
    engine = text_to_speech_engine(text_path, rate)
    engine.TTS()

if __name__ == "__main__":
    main()