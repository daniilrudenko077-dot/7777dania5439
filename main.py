import telebot

TOKEN = "8829102392:AAGCagyMADKivjqmxvHZvo12kFsBGwaXUww"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привіт! Я твій бот, і я працюю!")

@bot.message_handler(func=lambda message: True)
def echo(message):
    bot.send_message(message.chat.id, f"Ти написав: {message.text}")

bot.infinity_polling()
