from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Replace for your token
TOKEN = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXX'


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    await update.message.reply_text(
        "Hola mi nombre es Guille Code Bot, un bot creado por @guille_code_\n\n"
        "Envia /social para conocer mis redes sociales.\n"
        "Envia /cancel para cerrar la conversación.\n"
    )

async def social(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /social is issued."""
    await update.message.reply_text(
        "Ig: [@guille_code_](https://www.instagram.com/guille_code_?igsh=bThkcnNqNG0zeGVh&utm_source=qr)\n"
        "X: [@guille_code_](https://twitter.com/@guille_code_)\n"
        "Tiktok: [@guille_code_](https://www.tiktok.com/@guille_code_?_t=8lMm2Kbg8Bx&_r=1)\n"
        "Youtube: [@guille_code_](https://www.youtube.com/@guille_code_)\n"
        "Facebook: [@guillermocode](https://www.facebook.com/guillermocode/)"
        , parse_mode='MarkdownV2'
    )

async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Cancel the conversation."""
    await update.message.reply_text(
        "Cuidate, nos vemos pronto."
    )


def main() -> None:
    """Run the bot."""
    application = Application.builder().token(TOKEN).build()

    # Add the command handlers to the bot
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("social", social))
    application.add_handler(CommandHandler("cancel", cancel))

    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    # Run the main function
    main()