import telebot

bot=telebot.TeleBot("6175289952:AAFinoInu7MZsrT2omm8V-vzVEuhbe5PEG4",parse_mode=None)



@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id,"Hellooo there🐳,\nAre you having a great day?")

@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.send_message(message.chat.id,"Whee!!🐳,\nHow can I help you?")

@bot.message_handler(func=lambda m:True)
def echo_all(message):
    bot.send_message(message.chat.id,"It is not a command🤨")

bot.infinity_polling()