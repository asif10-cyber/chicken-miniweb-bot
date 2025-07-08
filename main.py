from telegram import Update, WebAppInfo, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from flask import Flask, send_from_directory
import threading

BOT_TOKEN = "6766692038:AAHY0CCG1di8s2i2G7xB0heB5aNa74CgyyU"
WEBAPP_URL = "https://<your-render-url>.onrender.com/static/chicken.html"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🐔 Open Chicken Game", web_app=WebAppInfo(url=WEBAPP_URL))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Welcome! Click below to open Chicken Game Mini App:", reply_markup=reply_markup)

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))

flask_app = Flask(__name__)

@flask_app.route('/static/<path:path>')
def static_file(path):
    return send_from_directory('static', path)

def run_flask():
    flask_app.run(host="0.0.0.0", port=8080)

def run_bot():
    app.run_polling()

if __name__ == '__main__':
    threading.Thread(target=run_flask).start()
    threading.Thread(target=run_bot).start()
