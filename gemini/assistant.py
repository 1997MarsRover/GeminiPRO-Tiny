import time
import google.generativeai as genai
from gtts import gTTS
from io import BytesIO
from pydub import AudioSegment
from pydub.playback import play
from config import GOOGLE_API_KEY



genai.configure(api_key=GOOGLE_API_KEY)

def generate_gemini_response(prompt):
    model = genai.GenerativeModel('gemini-pro')
    start_time = time.time()
    
    try:
        response = model.generate_content(prompt)
    except Exception as e:
        # Handle exceptions, e.g., API errors
        print(f"Error: {e}")
        return None, 0
    
    end_time = time.time()
    total_time = end_time - start_time
    print(f"Execution time: {total_time:.2f} seconds")
    print(f"Gemini response: {response}")
    return response, total_time

def convert_text_to_speech(text):
    tts = gTTS(text=text, lang='en')
    audio_data = BytesIO()
    tts.write_to_fp(audio_data)
    audio_data.seek(0)
    
    audio = AudioSegment.from_mp3(audio_data)

    
    play(audio)

def main():
    while True:
        gemini_prompt = input("Enter a prompt (type 'exit' to stop): ")
        
        if gemini_prompt.lower() == 'exit':
            break

        print(f"Gemini Prompt: {gemini_prompt}")

        gemini_response, execution_time = generate_gemini_response(gemini_prompt)

        if gemini_response:
            gemini_text = gemini_response.text
            print(f"Gemini Response: {gemini_text}")

            convert_text_to_speech(gemini_text)

if __name__ == "__main__":
    main()