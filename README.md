# GeminiPRO-Tiny
Run GeminiPro-Tiny on your local environment.
Load google-generativeai 
```bash
!pip install -q -U google-generativeai

```

Create a GOOGLE_API_KEY from [Google AI Studio](https://makersuite.google.com/app/apikey) and save it your config.py
```python
GOOGLE_API_KEY = <your api secret>
```
You can also test your API Secret with:
```bash
curl \
-H 'Content-Type: application/json' \
-d '{ "prompt": { "text": "Write a story about a magic backpack"} }' \
"https://generativelanguage.googleapis.com/v1beta3/models/text-bison-001:generateText?key=YOUR_API_KEY"
```
Now run prompts on Gemini..

```bash
Enter prompt here >> what is life
```



```python
response.text
```
Gemini Execution time is roughly **7.57s**, which is optimal, but am sure it can get even faster.

```yaml
Execution time: 7.57 seconds
Gemini response: <google.generativeai.types.generation_types.GenerateContentResponse object at 0x00000280DEF04D30>
Life is a complex and multifaceted concept that has been pondered by philosophers, scientists, and artists for centuries. While there is no single, universally agreed-upon definition of life, some common themes that emerge include:

1. **Organization**: Life is characterized by a high level of organization, from the molecular to the cellular to the organismal level. Living organisms are composed of complex structures that work together to maintain homeostasis and carry out various functions.

2. **Reproduction**: Life has the ability to reproduce itself, passing on genetic information to offspring. This process ensures the continuation of the species and allows for genetic variation and evolution.

3. **Metabolism**: Life requires energy to function and grow. This energy is obtained through metabolism, the process by which organisms convert nutrients into energy and use it to power their activities.

4. **Responsiveness**: Life is characterized by the ability to respond to stimuli in the environment. This includes both internal stimuli, such as hunger or thirst, and external stimuli, such as light, heat, or touch.

5. **Growth and Development**: Life involves growth and development over time. Organisms start out as small, simple entities and gradually grow and mature into more complex forms.

6. **Adaptation**: Life is capable of adapting to changes in the environment. This process, known as adaptation, allows organisms to survive and thrive in a wide range of conditions.

7. **Evolution**: Life evolves over time. This process, driven by natural selection, results in the gradual accumulation of beneficial traits that increase an organism's chances of survival and reproduction.

In addition to these core characteristics, life is often associated with concepts such as consciousness, intelligence, and purpose. However, these aspects of life are more subjective and controversial, and there is no scientific consensus on their precise nature or definition.

Ultimately, the question of what is life remains a complex and fascinating one, with no single answer that can fully capture the essence of this remarkable phenomenon.
```
Getting the prompt feedback.
```yaml
safety_ratings {
  category: HARM_CATEGORY_SEXUALLY_EXPLICIT
  probability: NEGLIGIBLE
}
safety_ratings {
  category: HARM_CATEGORY_HATE_SPEECH
  probability: NEGLIGIBLE
}
safety_ratings {
  category: HARM_CATEGORY_HARASSMENT
  probability: NEGLIGIBLE
}
safety_ratings {
  category: HARM_CATEGORY_DANGEROUS_CONTENT
  probability: NEGLIGIBLE
}
```
