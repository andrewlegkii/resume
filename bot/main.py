import logging
import os
import speech_recognition as sr
# import requests
from telegram import Bot, InputFile, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler, Filters
# from io import BytesIO

# Токен бота
TOKEN = '6602648869:AAEx80uLkmGudxzSAZ6TqKg4w9f8szaXuuI'

bot = Bot(token=TOKEN)

# Инициализация логгирования
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Обработчик команды /start
def start(update, context):
    user = update.message.from_user
    keyboard = [
        [InlineKeyboardButton("Посмотреть фото", callback_data='photo')],
        [InlineKeyboardButton("Другое фото", callback_data='otherphoto')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(f"Привет, {user.first_name}! Я бот, который поможет познакомиться с Легким Андеем. Чем могу помочь?", reply_markup=reply_markup)

# Кнопки
def button(update, context):
    query = update.callback_query
    if query.data == 'photo':
        send_photo(query, context)
    elif query.data == 'otherphoto':
        send_other_photo(query, context)

# Обработчик команды /photo
def send_photo(update, context):
    chat_id = update.message.chat.id
    photo_url = "https://disk.yandex.com.am/i/afo3s5e6HRJssw"
    context.bot.send_photo(chat_id=chat_id, photo=photo_url)

# Обработчик команды /otherphoto
def send_other_photo(update, context):
    chat_id = update.message.chat.id
    other_photo_url = "https://disk.yandex.com.am/i/kiZCI1QoQTrFgw"
    context.bot.send_photo(chat_id=chat_id, photo=other_photo_url)

# Обработчик команды /post
def send_post(update, context):
    update.message.reply_text("Всем привет! Меня зовут Легкий Андрей! Я увлекаюсь программированием и спортом.")

def list_files_in_directory(directory):
    files = os.listdir(directory)
    for file in files:
        print(file)

# Обработчик команды /voice (gpt)
def send_voice(update, context):
    chat_id = update.message.chat_id
    audio_folder = r"C:\Python\res\resume\bot"
    list_files_in_directory(audio_folder)

    for i in range(1):
        voice_file_path = os.path.join(audio_folder, "gran.ogg".format(i+1))
        
        if os.path.exists(voice_file_path):
            try:
                with open(voice_file_path, "rb") as voice_file:
                    context.bot.send_voice(chat_id=chat_id, voice=InputFile(voice_file))
            except Exception as e:
                print(f"Error sending voice: {e}")
        else:
            print(f"Voice file not found: {voice_file_path}")

# Обработчик команды /othervoice (sql/nosql)
def send_other_voice(update, context):
    chat_id = update.message.chat_id
    audio_folder = r"C:\Python\res\resume\bot"
    list_files_in_directory(audio_folder)

    for i in range(1):
        voice_file_path = os.path.join(audio_folder, "sql.ogg".format(i+1))
        
        if os.path.exists(voice_file_path):
            try:
                with open(voice_file_path, "rb") as voice_file:
                    context.bot.send_voice(chat_id=chat_id, voice=InputFile(voice_file))
            except Exception as e:
                print(f"Error sending voice: {e}")
        else:
            print(f"Voice file not found: {voice_file_path}")

# Обработчик команды /anothervoice (love)
def send_another_voice(update, context):
    chat_id = update.message.chat_id
    audio_folder = r"C:\Python\res\resume\bot"
    list_files_in_directory(audio_folder)

    for i in range(1):
        voice_file_path = os.path.join(audio_folder, "love.ogg".format(i+1))
        
        if os.path.exists(voice_file_path):
            try:
                with open(voice_file_path, "rb") as voice_file:
                    context.bot.send_voice(chat_id=chat_id, voice=InputFile(voice_file))
            except Exception as e:
                print(f"Error sending voice: {e}")
        else:
            print(f"Voice file not found: {voice_file_path}")

def process_voice(update, context):
    chat_id = update.message.chat_id
    voice_message = update.message.voice

    if voice_message:
        # Получаем файл аудиозаписи
        voice_file = context.bot.get_file(voice_message.file_id)
        voice_file.download('temp_voice.ogg')  # Загружаем аудиозапись на сервер

        try:
            recognizer = sr.Recognizer()
            with sr.AudioFile('temp_voice.ogg') as source:
                audio = recognizer.record(source)
            recognized_text = recognizer.recognize_google(audio, language="en-EN")

            context.bot.send_message(chat_id=chat_id, text=f"Распознанный текст: {recognized_text}")
        except Exception as e:
            context.bot.send_message(chat_id=chat_id, text=f"Ошибка распознавания голоса: {e}")

        # Удаляем временный файл
        os.remove('temp_voice.ogg')
    else:
        context.bot.send_message(chat_id=chat_id, text="Не удалось получить голосовое сообщение.")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("photo", send_photo))
    dp.add_handler(CommandHandler("otherphoto", send_other_photo))
    dp.add_handler(CommandHandler("post", send_post))
    dp.add_handler(CommandHandler("voice", send_voice))
    dp.add_handler(CommandHandler("othervoice", send_other_voice))
    dp.add_handler(CommandHandler("anothervoice", send_another_voice))
    dp.add_handler(CallbackQueryHandler(button))
    dp.add_handler(MessageHandler(Filters.voice, process_voice))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
