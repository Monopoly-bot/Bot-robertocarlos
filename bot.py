from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, CallbackContext
import asyncio

# Function to handle the /start command
async def start(update: Update, context: CallbackContext) -> None:
    # Define the buttons with links
    keyboard = [
        [InlineKeyboardButton("Google", url="https://www.google.com")],
        [InlineKeyboardButton("GitHub", url="https://www.github.com")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Send a message with buttons
    await update.message.reply_text(
        text="Welcome to the bot! Choose one of the options below:",
        reply_markup=reply_markup
    )

# Main function to run the bot
async def main():
    # Insert your BotFather token here
    TOKEN = "7818231062:AAGdNO37LZzT1kpnhX8M4sD0sE9XjSeH8Co"

    # Create the Application
    application = Application.builder().token(TOKEN).build()

    # Add the /start command handler
    application.add_handler(CommandHandler("start", start))

    # Start the bot
    print("Bot is running...")
    await application.run_polling()

# Handle the running event loop
if __name__ == "__main__":
    try:
        asyncio.run(main())
    except RuntimeError as e:
        if "running event loop" in str(e):
            loop = asyncio.get_event_loop()
            loop.run_until_complete(main())
        else:
            raise




