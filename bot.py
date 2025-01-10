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

# Main function to initialize and run the bot
async def main():
    TOKEN = "YOUR_BOT_TOKEN"  # Replace with your BotFather token
    application = Application.builder().token(TOKEN).build()

    # Add the /start command handler
    application.add_handler(CommandHandler("start", start))

    print("Bot is running...")
    # Run the bot using the current event loop
    await application.run_polling()

if __name__ == "__main__":
    # Ensure compatibility with Render's running event loop
    try:
        asyncio.run(main())
    except RuntimeError as e:
        if "This event loop is already running" in str(e):
            loop = asyncio.get_event_loop()
            loop.create_task(main())
            loop.run_forever()











