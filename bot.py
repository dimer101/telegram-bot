from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = '7976246852:AAFTmbrOvXHYM0wiJahEnPu2l_SMrBJgFRE'

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton(" Получить награду💰 ", url="https://dimer101.github.io/phantom_test0/")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text("Привет!", reply_markup=reply_markup)
    await update.message.reply_photo(photo="blob:https://web.telegram.org/af61e291-7c6e-41c4-bd8d-8085c6d976ab")

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

if __name__ == '__main__':
    main()
