import pathlib, textwrap,time 
from config import GOOGLE_API_KEY
import google.generativeai as genai
from IPython.display import display, Markdown
from Speech.Text_to_speech.text_to_speech import text_to_speech_engine as tts
# Used to securely store your API key
genai.configure(api_key=GOOGLE_API_KEY)

def to_markdown(text):
    if isinstance(text, str):
        text = text.replace('•', '  *')
        return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))
    elif isinstance(text, list):
        # Handle cases where text is a list, such as feedback with multiple entries
        formatted_text = "\n".join(item.replace('•', '  *') for item in text)
        return Markdown(textwrap.indent(formatted_text, '> ', predicate=lambda _: True))
    else:
        return Markdown(f"Unsupported type for conversion: {type(text)}")

def prompt(text: str):
    """
    Function to interact with the Generative AI model.
    
    Args:
    text (str): The input text prompt.
    
    Returns:
    tuple: A tuple containing the generated response and the total execution time.
    """
    model = genai.GenerativeModel('gemini-pro')
    start_time = time.time()
    
    try:
        response = model.generate_content(text)
    except Exception as e:
        # Handle exceptions, e.g., API errors
        print(f"Error: {e}")
        return None, 0
    
    end_time = time.time()
    total_time = end_time - start_time  
    print(f"Execution time: {total_time:.2f} seconds")
    print(f"Gemini response: {response}")
    return response, total_time
def chat_inf():
    gemini = "Hi, I am Gemini. How can I help you today?"
    print(gemini)
    while True:
        response, total_time = prompt(input("Enter prompt here >> "))
        if response:
            print(response.text)
            tts_engine = tts(response.text, 150)
            tts_engine.TTS()
            
            # Check if 'prompt_feedback' exists in the response object
            prompt_feedback = getattr(response, 'prompt_feedback', None)
            
            if prompt_feedback:
                #print(prompt_feedback)
                safety_ratings = prompt_feedback.safety_ratings
            else:
                print("No prompt feedback available.")
def main():
    chat_inf()

if __name__ == "__main__":
    main()