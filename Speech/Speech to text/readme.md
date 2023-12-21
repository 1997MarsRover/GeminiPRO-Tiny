Install vosk using pip [vosk](https://pypi.org/project/vosk/)
Download the Vosk model here [Vosk model(small-en-us)](https://drive.google.com/drive/folders/105F7L097LyHvEXYh5RzDf-F6dTmhxXTg?usp=sharing)

Other vosk model can be found at [Vosk Models](https://alphacephei.com/vosk/models)

Run the following to know your machine microphone index:
```python
import pyaudio

p = pyaudio.PyAudio()
for i in range(p.get_device_count()):
    info = p.get_device_info_by_index(i)
    print(f"Device Index: {info['index']} Device Name: {info['name']}")
```
