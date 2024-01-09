import cv2
import time
import google.generativeai as genai
import pyttsx3
import logging as log
from config import GOOGLE_API_KEY
import gradio as gr 
# Used to securely store your API key
genai.configure(api_key=GOOGLE_API_KEY)

class TextToSpeechEngine:
    def __init__(self, rate):
        self.rate = rate
        self.engine = pyttsx3.init()

    def tts(self, text):
        self.engine.setProperty('rate', self.rate)
        self.engine.say(text)
        self.engine.runAndWait()
        
class BlindAssistanceSystem:
    def __init__(self, model, tts_engine, interval_seconds=20):
        self.model = model
        self.tts_engine = tts_engine
        self.interval_seconds = interval_seconds
        self.blind_assistance_prompt = (
            "Describe the surroundings briefly and suggest the optimal way forward for a visually impaired person briefly, act as a navigation assistant and don't mention you are helping a visually impaired person; just give the way forward in Kiswahili."
        )
        self.assist_button_pressed = False

    def generate_text_and_tts(self, image):
        if self.assist_button_pressed:
            # Convert image data to numpy array
            frame = cv2.imdecode(image, 1)
            response = self.model.generate_content(
                contents=[self.blind_assistance_prompt, {'mime_type': 'image/jpeg', 'data': cv2.imencode('.jpg', frame)[1].tobytes()}]
            )
            generated_text = response.text
            print(f"Generated Text: {generated_text}")

            # Text-to-Speech
            self.tts_engine.tts(generated_text)

            # Wait for the specified interval before capturing the next frame
            time.sleep(self.interval_seconds)

    def set_assist_button_state(self, state):
        self.assist_button_pressed = state

def gr_interface(model, tts_engine, assist_system):
    iface = gr.Interface(
        fn=assist_system.generate_text_and_tts,
        inputs="image",
        outputs=None,
        live=True,
        examples=[["<your_example_image_url>"]],
        interpretation="dashboard",
        live_preview=True
    )

    assist_button = gr.Button(
        assist_system.set_assist_button_state,
        label="Assist",
        live=True
    )

    iface.launch([assist_button])

if __name__ == "__main__":
    model = genai.GenerativeModel('gemini-pro-vision')
    tts_engine = TextToSpeechEngine(rate=150)

    assist_system = BlindAssistanceSystem(model, tts_engine)

    gr_interface(model, tts_engine, assist_system)