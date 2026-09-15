import telebot
from telebot import types

# 1. Вставити токен, отриманий від @BotFather
TOKEN = 8829102392:AAGCagyMADKivjqmxvHZvo12kFsBGwaXUww
bot = telebot.TeleBot(TOKEN)

# Обробка команди /start
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("💡 Про проєкт")
    btn2 = types.KeyboardButton("🚀 Допомога")
    markup.add(btn1, btn2)
    
    bot.send_message(
        message.chat.id, 
        f"Привіт, {message.from_user.first_name}! Я AI-помічник. Оберіть дію з меню нижче:", 
        reply_markup=markup
    )

# Обробка текстових кнопок та повідомлень
@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text == "💡 Про проєкт":
        bot.send_message(message.chat.id, "Цей бот створений у рамках практичної роботи з AI Core.")
    elif message.text == "🚀 Допомога":
        bot.send_message(message.chat.id, "Бот працює в тестовому режимі. Надішли будь-яке повідомлення, і я продублюю його.")
    else:
        bot.send_message(message.chat.id, f"Ви написали: {message.text}")

# Запуск бота
if __name__ == "__main__":
    print("Бот запущений...")
    bot.infinity_polling()
