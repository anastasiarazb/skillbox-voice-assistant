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
        print('Скажите что-то >>>')
        audio = voice_recognizer.listen(source)

    try:
        voice_text = voice_recognizer.recognize_google(audio, language='ru')
        print(f'Вы сказали: {voice_text}')
        return voice_text
    except sr.UnknownValueError:
        return 'Ошибка распознавания'
    except sr.RequestError:
        return 'Ошибка запроса'


def say(text):
    voice = gTTS(text, lang='ru')
    file = 'audio.mp3'
    voice.save(file)

    playsound.playsound(file)

    os.remove(file)

    print(f'Ассистент: {text}')


def handle_command(command):
    command = command.lower()

    if command == 'привет':
        say("Привет-привет!")
    elif command == 'пока':
        stop()
    else:
        say('Не понятно, повторите')


def stop():
    say('До скорого')
    exit()


def start():
    print('Запуск ассистента...')

    while True:
        # print('Жду команды')
        command = listen()
        handle_command(command)
        # print(f'Command: {command}')


try:
    start()
except KeyboardInterrupt:
    stop()


# 1) Мы в цикле запускаем функцию, которая обрабатывает взодные данные:
# start(): listen() + handle_command()
#      2) listen(): user audio -> user text
#      3) handle_command(): user text -> robot text -> say()
#         4) say(): robot text -> robot audio