from telegram import Bot
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

TOKEN = "TOKEN_BOT_ANDA"

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Selamat datang! Gunakan /check <username> untuk memeriksa ketersediaan username.')

def check_username(update: Update, context: CallbackContext) -> None:
    if len(context.args) == 0:
        update.message.reply_text('Gunakan perintah ini dengan format: /check <username>')
        return

    username_to_check = context.args[0]
    bot = Bot(token=TOKEN)
    user = bot.get_chat(username=username_to_check)

    if user:
        update.message.reply_text(f'@{username_to_check} sudah digunakan.')
    else:
        update.message.reply_text(f'@{username_to_check} tersedia!')

def main() -> None:
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("check", check_username))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()