import telebot
import config

#Токен связывающий код с ботом
bot = telebot.TeleBot(config.TOKEN)
#core.telegram.org/bots/api - документация для бота

#Приветственное сообщение
@bot.message_handler(commands=['start'])
def start_message(message):
	bot.send_message(message.chat.id, "Привед медвед, {0.first_name}!\nЯ - <b>{1.first_name}</b>, тестовый <b>бот</b> созданый таким же Бедолагой.".format(message.from_user, bot.get_me()), parse_mode = 'html')

# Сообщение ответчик
@bot.message_handler(content_types=['text'])
def telegram_bot(message):
	bot.send_message(message.chat.id, message.text)

bot.polling()