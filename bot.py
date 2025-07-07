from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = '7976246852:AAFTmbrOvXHYM0wiJahEnPu2l_SMrBJgFRE'  # Никогда не публикуй настоящий токен в открытом виде!

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton(" Получить награду💰 ", url="https://dimer101.github.io/phantom_test0/")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_photo(
        photo="https://i.postimg.cc/fy7h0Wgj/temp-Image0hc-CGf.avif",
        caption="(◕‿◕)",  # Подпись под изображением + кнопка
        reply_markup=reply_markup
    )

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

if __name__ == '__main__':
    main()
