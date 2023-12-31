# VoiceBot

VoiceBot - это пример бота для Telegram, написанного на Python с использованием библиотеки `python-telegram-bot` и `SpeechRecognition`. Этот бот демонстрирует, как создать телеграм-бота, который может отвечать на команды пользователя, отправлять фотографии и даже распознавать голосовые команды, которые пользователи отправляют ему.

## Особенности

- Команда `/start` - начало общения с ботом. Бот предлагает пользователю выбрать действие с помощью кнопок.
- Команда `/photo` - бот отправляет фотографию, предоставленную по указанному URL.
- Команда `/otherphoto` - бот отправляет другую фотографию с другим URL.
- Команда `/post` - бот отправляет текстовое сообщение о себе.
- Команда `/voice` - бот отправляет аудиозапись в формате ogg.
- Команда `/othervoice` - бот отправляет другую аудиозапись в формате ogg.
- Команда `/anothervoice` - бот отправляет третью аудиозапись в формате ogg.
- Команда `/github` - бот отправляет ссылку на мой публичный репозиторий.

## Распознавание голосовых команд

- Бот также может распознавать голосовые команды, отправленные пользователем.
- При отправке голосового сообщения, бот загружает аудиозапись, а затем использует библиотеку `SpeechRecognition` для распознавания речи и отправки распознанного текста обратно пользователю.

## Запуск бота

1. Установите необходимые зависимости, выполнив:

```bash
pip install -r requirements.txt
```

2. Создайте файл `.env` и запишите там свой токен.

3. Запустите бота:

```bash
python main.py
```
