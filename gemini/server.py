import cv2
import time
import google.generativeai as genai
import pyttsx3
import gradio as gr
from config import GOOGLE_API_KEY

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
    def __init__(self, model, tts_engine):
        self.model = model
        self.tts_engine = tts_engine
        self.blind_assistance_prompt = (
            "Describe the surroundings briefly and suggest the optimal way forward for a visually impaired person briefly, act as a navigation assistant and don't mention you are helping a visually impaired person; just give the way forward in Kiswahili."
        )

    def generate_text_and_tts(self, image):
        # Convert image data to numpy array
        frame = cv2.imdecode(image, 1)
        response = self.model.generate_content(
            contents=[self.blind_assistance_prompt, {'mime_type': 'image/jpeg', 'data': cv2.imencode('.jpg', frame)[1].tobytes()}]
        )
        generated_text = response.text
        print(f"Generated Text: {generated_text}")

        # Text-to-Speech
        self.tts_engine.tts(generated_text)

def gr_interface(model, tts_engine):
    blind_system = BlindAssistanceSystem(model, tts_engine)

    iface = gr.Interface(
        fn=blind_system.generate_text_and_tts,
        inputs="image",
        outputs=None,
        live=True,
    )

    iface.launch(share=True)

if __name__ == "__main__":
    model = genai.GenerativeModel('gemini-pro-vision')
    tts_engine = TextToSpeechEngine(rate=150)

    gr_interface(model, tts_engine)