#
# Пример приложения голосового ассистента
#
import speech_recognition as sr
import random
import playsound
import os
from gtts import gTTS


def listen():
    voice_recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Скажите что-то >>> ")
        audio = voice_recognizer.listen(source)

    try:
        voice_text = voice_recognizer.recognize_google(audio, language='ru')
        print(f'Вы сказали: {voice_text}')
        return voice_text

    except sr.UnknownValueError:
        return "ошибка распознавания"
    except sr.RequestError:
        return "ошибка запроса"


def say(text):
    voice = gTTS(text, lang='ru')
    file = "audio_" + str(random.randint(0, 10000)) + ".mp3"
    voice.save(file)

    playsound.playsound(file)
    os.remove(file)

    print(f'Ассистент: {text}')


def handle_command(command):
    command = command.lower()

    if command == "привет":
        say("Привет-привет")
    elif command == "пока":
        stop()
    else:
        say("Не понятно, повторить")


def stop():
    say("До скорого")
    exit()


def start():
    print('Запуск ассистента...')

    while True:
        command = listen()
        handle_command(command)


try:
    start()
except KeyboardInterrupt:
    stop()
