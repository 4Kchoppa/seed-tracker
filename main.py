import telebot
import os

BOT_TOKEN = "7935840724:AAHZpTPvgbZ_7dALnRPAKy1cOkzt89OkAOA"
OWNER_ID = 5933245731

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    if message.from_user.id == OWNER_ID:
        bot.reply_to(message, "👋 Welcome back, boss! Your Seed Tracker Bot is online.")
    else:
        bot.reply_to(message, "🚫 You are not authorized to use this bot.")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if message.from_user.id == OWNER_ID:
        bot.reply_to(message, f"📥 Received: {message.text}")
    else:
        bot.reply_to(message, "❌ Access denied.")

bot.infinity_polling()