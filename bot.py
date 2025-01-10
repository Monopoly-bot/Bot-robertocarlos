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

# Function to initialize and run the bot
async def main():
    TOKEN = "7818231062:AAGdNO37LZzT1kpnhX8M4sD0sE9XjSeH8Co"  # Replace with your BotFather token
    application = Application.builder().token(TOKEN).build()

    # Add the /start command handler
    application.add_handler(CommandHandler("start", start))

    print("Bot is running...")
    # Start the bot with polling
    await application.run_polling()

if __name__ == "__main__":
    # Use the current event loop
    try:
        asyncio.get_event_loop().run_until_complete(main())
    except KeyboardInterrupt:
        print("Bot stopped.")











