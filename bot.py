
import os
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = os.environ["BOT_TOKEN"]
bot = telebot.TeleBot(TOKEN)

ADMIN = "mizual_0"

courses = [
    ("Мини-продукт", "1 000 ₽ / $20"),
    ("8 поток отдельно", "1 500 ₽ / $25"),
    ("9 поток отдельно", "1 500 ₽ / $25"),
    ("Полный VIP-курс", "2 000 ₽ / $30"),
]

@bot.message_handler(commands=["start"])
def start(message):
    markup = InlineKeyboardMarkup()
    for i, (name, price) in enumerate(courses):
        markup.add(InlineKeyboardButton(
            f"{name} — {price}", callback_data=f"course_{i}"
        ))
    bot.send_message(
        message.chat.id,
        "🖤 BLACK P2P Academy\n\nВыбери обучение:",
        reply_markup=markup
    )

@bot.callback_query_handler(func=lambda call: call.data.startswith("course_"))
def choose_course(call):
    i = int(call.data.split("_")[1])
    name, price = courses[i]
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(
        "💬 Написать для оплаты",
        url=f"https://t.me/{ADMIN}"
    ))
    bot.answer_callback_query(call.id)
    bot.send_message(
        call.message.chat.id,
        f"🖤 {name}\nЦена: {price}\n\nДля оплаты и получения доступа напиши администратору.",
        reply_markup=markup
    )

bot.infinity_polling()
