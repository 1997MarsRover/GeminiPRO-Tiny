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
            engine = pyttsx3.init()
            engine.setProperty('rate', self.rate)
            log.info(self.text_path)
            log.info(engine.getProperty('rate'))
            engine.say(self.text_path)
            engine.runAndWait()
            engine.stop()