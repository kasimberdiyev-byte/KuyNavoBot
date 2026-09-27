from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "import os

TOKEN = os.getenv("BOT_TOKEN")"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎵 Salom! Men Kuy Navo Music Botman.\n"
        "Qo‘shiq nomini yuboring."
    )

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

print("Bot ishga tushdi...")
app.run_polling()