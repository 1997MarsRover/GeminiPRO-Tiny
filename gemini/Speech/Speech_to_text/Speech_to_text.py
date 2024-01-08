import wave
import sys
import pyaudio as pa
import speech_recognition as sr
from vosk import Model, KaldiRecognizer, SetLogLevel
import json

class speech_to_text_engine:
    def __init__ (self, model_path, model_name, lang,save_textfile_dir):
        self.model_path = model_path
        self.model_name = model_name
        self.lang = lang
        self.save_textfile_dir = save_textfile_dir
    
    def config(self):
        model = Model(model_path = self.model_path, model_name=self.model_name, lang=self.lang)
        
        SetLogLevel(0)
        p = pa.PyAudio()
        # open a stream with the system microphone as the input source
        mic_index = 3
        stream = p.open(format=pa.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000, input_device_index=mic_index)
        stream.start_stream()

        rec = KaldiRecognizer(model, 16000)
        rec.SetWords(True)
        rec.SetPartialWords(True)

        recognized_text = ""
        r = sr.Recognizer()
        return stream, rec, recognized_text

    def realtimelisten(self, stream = None ):
        # Capture audio from the microphone and perform real-time speech recognition
        stream,rec, recognized_text = self.config()
        while True:
            #data = wf.readframes(4000)
            print("start talking")

            #  read audio data from the microphone
            data = stream.read(4000,exception_on_overflow=False)

            #  check if there is no more
            if len(data) == 0:
                break
            #  Process the audio data using the KaldiRecognizer
            rec.AcceptWaveform(data)
            #  Get the partial recognition result
            partial_result = rec.PartialResult()
            if partial_result:
                partial_text = json.loads(partial_result).get("partial", "")
                recognized_text += partial_text 
                print("Partial Result:", partial_text)

        # Save the recognized text to a file
        with open(self.save_textfile_dir, "w") as output_file:
            output_file.write(recognized_text)

        #  Get the final result after the loop ends
        final_result = rec.FinalResult()
        final_text = json.loads(final_result)
        print(final_text)

        #Stop and close the audio stream
        #print(rec.FinalResult())
        stream.stop_stream()
        stream.close()
        #terminate Audio
        p.terminate()

        print(f"Recognized text saved to: {self.save_textfile_dir}")

    def listen_for_command(self):
        with sr.Microphone() as source:
            print("Listening for command...")
            audio = r.listen(source)
        try:
            command = r.recognize_google(audio).lower()
            print("Command:", command)
            return command
        except sr.UnknownValueError:
            print("Could not understand audio.")
            return None



def main():
    model_path = "D:\\vizuosense_mine\\STT\\Resources\\vosk-model-small-en-us-0.15"
    model_name = "vosk-model-small-en-us-0.15"
    language = "small-en-us"
    save_textfile_dir = "D:\\vizuosense_mine\\STT\\Resources\\test.txt"
    engine = speech_to_text_engine(model_path, model_name, language, save_textfile_dir)
    engine.realtimelisten()

if __name__ == "__main__":
    main()
