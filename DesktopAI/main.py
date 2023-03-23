import openai
import speech_recognition as sr
import pyttsx3

openai.api_key = "OPENAI_KEY"
key_phrase = "OK Genesis"


def virtual_assistant():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    input_text = r.recognize_google(audio)
    print(f"You said: {input_text}")

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=input_text,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5
    ).choices[0].text

    eng = pyttsx3.init()
    voice = eng.getProperty('voices')
    eng.setProperty('voice', voice[1].id)
    print(response)
    eng.say(response)
    eng.runAndWait()


while True:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        if r.recognize_google(audio) == key_phrase:
            virtual_assistant()
    except sr.UnknownValueError:
        pass
    except sr.RequestError as e:
        print("Error:", e)
