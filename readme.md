# Голосовой помощник на Python

Данный проект содержит примеры кода с вебинара SkillBox.

**Структура проекта**:

- **app**: исходный код голосового помощника
- **resources**: материалы с вебинара
- **src**: небольшие примеры программ с вебинара

## Установка зависимостей

Для корректной работы приложения необходимо установить несколько дополнительных модулей Python через терминал / командную строку.

#### Распознавание голоса

Для установки выполнить команду - `pip install SpeechRecognition`

#### Захват звука с микрофона

Для установки выполнить команду - `pip install PyAudio`

* Для владельцев Linux (Ubuntu) предварительно выполнить - `sudo apt-get install python3-audio`
* Для владельцев macOS предварительно выполнить (понадобится инструмент [Homebrew](https://brew.sh/)) - `brew install portaudio`

#### Преобразование текста в аудио

Для установки выполнить команду - `pip install gTTS`

#### Воспроизведение звука

Для установки выполнить команду - `pip install PlaySound`

* Для владельцев macOS предварительно выполнить - `pip install PyObjC`