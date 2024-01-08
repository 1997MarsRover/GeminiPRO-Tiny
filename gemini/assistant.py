import cv2
import time
from pathlib import Path
import google.generativeai as genai
import pyttsx3
import json
import logging as log
from config import GOOGLE_API_KEY

# Used to securely store your API key
genai.configure(api_key=GOOGLE_API_KEY)

# Predefined prompt for assisting a blind person
blind_assistance_prompt = "Describe the surroundings briefly and suggest the optimal way forward for a visually impaired person briefly, act as a navigation assistant and don't mention you are helping a visually impaired person; just give the way forward."

class text_to_speech_engine():
    def __init__(self, rate):
        self.rate = rate

    def TTS(self, text):
        engine = pyttsx3.init()
        engine.setProperty('rate', self.rate)
        log.info(text)
        log.info(engine.getProperty('rate'))
        engine.say(text)
        engine.runAndWait()
        engine.stop()

def capture_and_generate(model, tts_engine, interval_seconds=20):
    while True:
        # Capture a frame from the camera
        cap = cv2.VideoCapture(0)  # Assuming camera index 0, you may need to adjust it
        ret, frame = cap.read()
        cap.release()  # Release the camera capture

        if not ret:
            print("Error: Unable to capture frame from the camera.")
            continue

        # Use the correct method signature for generate_content
        response = model.generate_content(
            contents=[blind_assistance_prompt, {'mime_type': 'image/jpeg', 'data': cv2.imencode('.jpg', frame)[1].tobytes()}]
        )

        generated_text = response.text
        print(f"Generated Text: {generated_text}")

        # Text-to-Speech
        tts_engine.TTS(generated_text)

        # Wait for the specified interval before capturing the next frame
        time.sleep(interval_seconds)

if __name__ == "__main__":
    # Create an instance of the GenerativeModel
    model = genai.GenerativeModel('gemini-pro-vision')

    # Create an instance of the text-to-speech engine
    tts_engine = text_to_speech_engine(rate=150)  # Adjust the rate as needed

    # Start capturing frames, generating content, and converting text to speech
    capture_and_generate(model, tts_engine)