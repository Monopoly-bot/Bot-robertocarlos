from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, CallbackContext
import asyncio

# Function to handle the /start command
async def start(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [InlineKeyboardButton("Google", url="https://www.google.com")],
        [InlineKeyboardButton("GitHub", url="https://www.github.com")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        text="Welcome to the bot! Choose one of the options below:",
        reply_markup=reply_markup
    )

# Function to initialize the bot
async def main():
    import os
    TOKEN = os.getenv("BOT_TOKEN")

    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))

    print("Bot is running...")
    await application.initialize()
    await application.start()
    await application.updater.start_polling()
    await application.updater.wait_for_stop()
    await application.stop()
    await application.shutdown()

if __name__ == "__main__":
    # Use the current event loop instead of asyncio.run()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())










