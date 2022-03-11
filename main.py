import os
import telebot

bot = telebot.TeleBOT("API Key Here")


@bot.message_handler(commands=["start"])
daf send_welcome(message):
 bot.reply_to(message,"Hi! I'm Art With Rusith Chat Bot")

@bot.message_handler(commands=["how"])
def send_message(message):
 bot.send_message(message,"https://www.youtube.com/channel/UCD8924Mgj1nqL0aBkZj84Jg")

bot.polling()