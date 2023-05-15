import random
import telebot
import khayyam
from gtts import gTTS
import qrcode

bot = telebot.TeleBot("Token", parse_mode= None)
bot_state = None

@bot.message_handler(commands= ["start"])
def start(message):
    global bot_state
    bot.reply_to(message, "Welcome 🐳" + message.from_user.first_name + "Please write \help to see the menu")


@bot.message_handler(commands= ["help"])
def help(message):
    global bot_state
    bot.reply_to(message, """ 
    /start
    Welcome...
    /game
    Play Gussing the number\n
    /age 
    Enter your date of birth (year/month/day) to calculate your age\n
    /voice 
    Type your an english sentence and the bot will read it for you \n
    /max
    Write a list of numbers devided by commas and the bot will determine the largest one \n
    /argmax 
    Write a list of numbers devided by commas and the bot will determine the index of the largest one \n
    /qrcode
    Type your sentence you want to be transformed to a QR code\n
    /help
    See the menue""")

@bot.message_handler(commands= ["game", "New_Game"])
def game(message):
    global bot_state
    global rand_num
    markup = telebot.types.ReplyKeyboardMarkup(row_width= 1)
    button = telebot.types.KeyboardButton("/New_Game")
    markup.add(button)
    rand_num = random.randint(1,100)
    bot.send_message(message.chat.id, "Enter a number between 0 and 100" , reply_markup=markup)
    
    

    @bot.message_handler(func= lambda m:True)
    def guess_game(message):
        global rand_num
        if int(message.text) < rand_num:
            bot.send_message(message.chat.id, "Go up ⏫", reply_markup=markup )
            
        elif int(message.text) > rand_num:
            bot.send_message(message.chat.id, "Go down ⏬", reply_markup= markup ) 
            
        elif int(message.text) == rand_num:
            bot.send_message(message.chat.id, " You won the game 🏆", reply_markup= telebot.types.ReplyKeyboardRemove(selective=True))

@bot.message_handler(commands= ["age"])
def age(message):
    global bot_state
    user_age = bot.send_message(message.chat.id, "Enter your date of birth (year/month/day)")
    bot.register_next_step_handler(user_age, age_calculator)

def age_calculator(message):
        date_of_birth = (str(message.text)).split("/")
        differnce = khayyam.JalaliDatetime.now() - khayyam.JalaliDatetime(date_of_birth[0], date_of_birth[1], date_of_birth[2])
        year = differnce.days // 365
        differnce = differnce.days % 365
        month = differnce // 30
        day = (differnce % 30) -7
        bot.send_message(message.chat.id, "Your exact age is: "+ str(year) + " years and "+ str(month) + " months and "+ str(day) + " days.")
        
@bot.message_handler(commands= ["voice"])
def voice(message):
    global bot_state
    user_txt = bot.send_message(message.chat.id, "Type your english sentence")
    bot.register_next_step_handler(user_txt, voice_maker)

def voice_maker(message):
    audio = gTTS(text = message.text, lang = "en", slow = False)
    audio.save("audio.mp3")
    audio_file = open("audio.mp3", "rb")
    bot.send_voice(message.chat.id, audio_file)

@bot.message_handler(commands= ["max"])
def max(message):
    global bot_state
    user_numbers = bot.send_message(message.chat.id, "Write a list of numbers devided by commas")
    bot.register_next_step_handler(user_numbers, max_finder)

def max_finder(message):
    numbers = message.text.split(",")
    maximum = 0
    for i in range (len(numbers)):
        if int(numbers[i]) > maximum:
            maximum = int(numbers[i])
    bot.send_message(message.chat.id, str(maximum) + " is the largest number")

@bot.message_handler(commands= ["argmax"])
def argmax(message):
    global bot_state
    user_numbers = bot.send_message(message.chat.id, "Write a list of numbers devided by commas")
    bot.register_next_step_handler(user_numbers, index_finder)

def index_finder(message):
    numbers = message.text.split(",")
    maximum = 0
    index = 0
    for i in range (len(numbers)):
        if int(numbers[i]) > maximum:
            maximum = int(numbers[i])
            index = i + 1
    bot.send_message(message.chat.id, "position of " + str(maximum) + " is: " + str(index))

@bot.message_handler(commands= ["qrcode"])
def QRcode(message):
    global bot_state
    user_txt = bot.send_message(message.chat.id, "Type an english sentence")
    bot.register_next_step_handler(user_txt, QR_maker)

def QR_maker(message):
    user_qrcode = qrcode.make(message.text)
    user_qrcode.save("QR.jpg")
    QR_file = open("QR.jpg", "rb")
    bot.send_photo(message.chat.id, QR_file)



bot.infinity_polling()
    
