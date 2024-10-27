
import requests
import json 
import telebot
import random
from telebot import types
print(f'''\033[33;103m
⠀⠀⠀⠀⣿⡇⠀⢸⣿⡇⠀⠀⠀⠀
⠸⠿⣿⣿⣿⡿⠿⠿⣿⣿⣿⣶⣄⠀
⠀⠀⢸⣿⣿⡇⠀⠀⠀⠈⣿⣿⣿⠀
⠀⠀⢸⣿⣿⡇⠀⠀⢀⣠⣿⣿⠟⠀
⠀⠀⢸⣿⣿⡿⠿⠿⠿⣿⣿⣥⣄⠀
⠀⠀⢸⣿⣿⡇⠀⠀⠀⠀⢻⣿⣿⣧
⠀⠀⢸⣿⣿⡇⠀⠀⠀⠀⣼⣿⣿⣿
⢰⣶⣿⣿⣿⣷⣶⣶⣾⣿⣿⠿⠛⠁
⠀⠀⠀⠀⣿⡇⠀⢸⣿⡇⠀⠀⠀⠀
''')


API_TOKEN = '7506082373:AAFX9wKHWTmL5AhO7zwNJmrW1TfqqO2g4dI'

bot = telebot.TeleBot(API_TOKEN)
TC4 = types.InlineKeyboardButton(text =" Dev🐉",url="tg://user?id=6268264542")
AIM = types.InlineKeyboardButton(text =" CH",url="https://t.me/Python_toolc")
X = types.InlineKeyboardButton(text ="Add me to a group",url="https://t.me/C4_S4_BOT?startgroup")
HLTV = types.InlineKeyboardButton(text ="Add me to a channel ",url="https://t.me/C4_S4_BOT?starTC4hannel")


@bot.message_handler(commands=['start'])
def start(message):
         C4_= types.InlineKeyboardMarkup()
         C4_.row_width = 2
         C4_.add(AIM,TC4,X,HLTV)
         photo = f"t.me/{message.from_user.username}"
         name_of_C4= f"{message.from_user.first_name}"
         text = f'''* مرحبا عزيزي * {name_of_C4}* انا بوت تفاعل برموز تعبيرية يمكنك اضافتي إلى كروب او قناة للتفاعل
*'''
         bot.send_photo(message.chat.id,photo,text ,
 parse_mode="Markdown",reply_markup=C4_)

@bot.message_handler(func=lambda message: True)
def start(message):
    reactions = ["👍", "❤️", "🔥", "🥰", "👏", "😁","❤️‍🔥","🤯","😘","👨‍💻","😎","🕊","🗿","😐","🙄","😒","😳","🕺","🌙","🫡","👻","🎂","🎀","🙈","🇪🇬","🤣","😂","🥹","🦅","💌","😉","😍","🫶🏻","☺️","💓","🤍","🪐","❔","❗","™️","⏳","📌","❤️‍🩹","💎","🩶","💚","💖","❣️","💝","🌚"]
    emoji = random.choice(reactions)
    response = send_message_react(
        {
            'chat_id': message.chat.id,
            'message_id': message.message_id,
            'reaction': json.dumps([{'type': "emoji", "emoji": emoji}])
        }
    )
    

def send_message_react(datas={}):
    url = "https://api.telegram.org/bot" + API_TOKEN + "/" + 'setmessagereaction'
    response = requests.post(url, data=datas)

    if response.status_code != 200:
        return "Error: " + response.text
    else:
        return response.json()

bot.infinity_polling()
