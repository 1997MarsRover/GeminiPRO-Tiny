import time
import google.generativeai as genai
import pyttsx3
import logging as log
from picamera import PiCamera
from io import BytesIO


# Configure Google AI with API key
genai.configure(api_key="AIzaSyA-gaD4q8UwEp2Z5yKZ0g0MZa7CoCVA1VU")

class TextToSpeechEngine:
    def __init__(self, rate):
        self.rate = rate
        self.engine = pyttsx3.init()

    def tts(self, text):
        self.engine.setProperty('rate', self.rate)
        log.info(text)
        log.info(self.engine.getProperty('rate'))
        self.engine.say(text)
        self.engine.runAndWait()

class BlindAssistanceSystem:
    def __init__(self, model, tts_engine, prompt_interval=20):
        self.model = model
        self.tts_engine = tts_engine
        self.prompt_interval = prompt_interval
        self.blind_assistance_prompt = (
            "you are a sarcastic Navigation assistant for a visual impaired person. What is the optimal way forward the person should take to avoid collision, only state the object you see if it is in the way of the person."
        )

    def capture_and_generate(self):
        with PiCamera() as camera:
            while True:
                stream = BytesIO()
                camera.capture(stream, format='jpeg')
                stream.seek(0)
                frame = stream.getvalue()

                if frame is not None:
                    # Generate content using the model
                    response = self.model.generate_content(
                        contents=[self.blind_assistance_prompt, {'mime_type': 'image/jpeg', 'data': frame}]
                    )

                    # Extract generated text and log it
                    generated_text = response.text
                    log.info(response.prompt_feedback)
                    log.info(f"Generated Text: {generated_text}")

                    # Convert generated text to speech
                    self.tts_engine.tts(generated_text)

                    # Wait for the specified interval before capturing the next frame
                    time.sleep(self.prompt_interval)

if __name__ == "__main__":
    # Create instances of the GenerativeModel and TextToSpeechEngine
    model = genai.GenerativeModel('gemini-pro-vision')
    tts_engine = TextToSpeechEngine(rate=150)

    # Create an instance of the BlindAssistanceSystem and start capturing and generating
    blind_system = BlindAssistanceSystem(model, tts_engine)
    blind_system.capture_and_generate()
