#
# Пример приложения голосового ассистента
#
import speech_recognition as sr
import playsound
import os
from gtts import gTTS

'''
Start: функция обрабатывает входные данные в цикле listen() + handle_command()
      listen: user speech -> user text
      handle_command: user text -> robot text -> say()
          say: robot text -> robot audio
'''


def listen():
    '''
    audio -> text
    '''

    voice_recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print('Скажите что-то >>>')
        audio = voice_recognizer.listen(source)


    try:
        voice_text = voice_recognizer.recognize_google(audio, language='ru')
        print(f'Вы сказали: {voice_text}')
        return voice_text
    except:
        return 'Ошибка'


def say(text):
    """
    text -> robot speech

    """
    voice = gTTS(text, lang='ru')
    file = 'audio.mp3'
    voice.save(file)
    playsound.playsound(file)
    os.remove(file)

    print(f'Ассистент: {text}')


def handle_command(command):
    command = command.lower()

    if command == 'привет':
        say('Привет-привет!')
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
        print('Жду команды')
        command = listen()
        handle_command(command)



try:
    start()
except KeyboardInterrupt:
    stop()
