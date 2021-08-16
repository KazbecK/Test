if message.chat.type == 'private':
    if message.text == '😄Как дела?':
        bot.send_message(message.chat.id, "Нормалёк👍, сам как?")
    else:
        bot.send_message(message.chat.id, "Пока непонимаю что написано(")


	#keyboard - нопки под сообщением бота
	markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
	item1 = types.KeyboardButton("😄Как дела?")
#	item2 = tyeps.KeyboardButton("⏱Какое сейчас время?")

markup.add(item1)