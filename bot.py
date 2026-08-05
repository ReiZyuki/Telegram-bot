import os
import telebot
import requests
import random
from concurrent.futures import ThreadPoolExecutor, as_completed

TOKEN = os.environ.get("TOKEN")
bot = telebot.TeleBot(TOKEN)

session = requests.Session()
session.headers.update({
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
})

@bot.message_handler(commands=['start', 'help'])
def start(message):
    bot.reply_to(message, "🔥 Bot Live on Railway\n\n/hentai\n/porn\n/manga <name> <chapter>")

@bot.message_handler(commands=['hentai', 'porn'])
def send_image(message):
    try:
        bot.send_chat_action(message.chat.id, "upload_photo")
        res = session.get("https://api.lolicon.app/setu/v2?r18=1&num=1", timeout=10)
        data = res.json()
        if data.get("data"):
            url = data["data"][0]["urls"]["original"]
            img = session.get(url, timeout=12)
            if img.status_code == 200:
                bot.send_photo(message.chat.id, img.content)
                return
        bot.reply_to(message, "Try again")
    except Exception as e:
        bot.reply_to(message, "Error, try again")

@bot.message_handler(commands=['manga'])
def manga(message):
    bot.reply_to(message, "Manga feature baad mein add karenge. Abhi /hentai use kar.")

print("Bot starting on Railway...")
bot.infinity_polling()
