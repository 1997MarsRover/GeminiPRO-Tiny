from config import GOOGLE_API_KEY
import cv2
import time
from pathlib import Path
import google.generativeai as genai

# Used to securely store your API key
genai.configure(api_key=GOOGLE_API_KEY)


# Predefined prompt for assisting a blind person
blind_assistance_prompt = "Describe the surroundings briefly and suggest the optimal way forward for a visually impaired person briefly, act a navigation assistant and dont mention you are helping a visually impaired person just give the way forward in kiswahili."
def capture_and_generate(model, interval_seconds=20):
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

        print(f"Generated Text: {response.text}")

        # Wait for the specified interval before capturing the next frame
        time.sleep(interval_seconds)

if __name__ == "__main__":
    # Create an instance of the GenerativeModel
    model = genai.GenerativeModel('gemini-pro-vision')

    # Start capturing frames and generating content
    capture_and_generate(model)