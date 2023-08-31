import logging
from telegram import Bot
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

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

# Обработчик команды /voice (gpt)
def send_voice(update, context):
    chat_id = update.message.chat_id
    for i in range(3):
        voice_url = "https://disk.yandex.com.am/d/MpfMKNlG1_fgHw_{}.ogg".format(i+1)
        context.bot.send_voice(chat_id=chat_id, voice=voice_url)

# Обработчик команды /othervoice (sql/nosql)
def send_other_voice(update, context):
    chat_id = update.message.chat_id
    for i in range(3):
        other_voice_url = "https://disk.yandex.com.am/d/aJoqIMXz7t34JA_{}.ogg".format(i+1)
        context.bot.send_voice(chat_id=chat_id, voice=other_voice_url)

# Обработчик команды /anothervoice (love)
def send_another_voice(update, context):
    chat_id = update.message.chat_id
    for i in range(3):
        another_voice_url = "https://disk.yandex.com.am/d/9r6szShI_fT2_g_{}.ogg".format(i+1)
        context.bot.send_voice(chat_id=chat_id, voice=another_voice_url)

def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("photo", send_photo))
    dp.add_handler(CommandHandler("otherphoto", send_other_photo))
    dp.add_handler(CommandHandler("post", send_post))
    dp.add_handler(CommandHandler("voice", send_voice))
    dp.add_handler(CommandHandler("othervoice", send_other_voice))
    dp.add_handler(CommandHandler("anothervoice", send_another_voice))
    dp.add_handler(CallbackQueryHandler(button))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
