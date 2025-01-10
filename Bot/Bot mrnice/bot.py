from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Funzione per gestire il comando /start
def start(update: Update, context: CallbackContext) -> None:
    # Crea i bottoni con link
    keyboard = [
        [InlineKeyboardButton("prova1", url="https://www.github.com")],
        [InlineKeyboardButton("prova2", url="https://www.github.com")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Messaggio di benvenuto con bottoni
    update.message.reply_text(
        "Benvenuto nel mio bot! Scegli un'opzione cliccando sui bottoni:",
        reply_markup=reply_markup
    )

# Funzione principale
def main():
    # Inserisci il tuo token fornito da BotFather
    TOKEN = "7818231062:AAGdNO37LZzT1kpnhX8M4sD0sE9XjSeH8Co"

    # Crea l'oggetto Updater
    updater = Updater(TOKEN)

    # Aggiungi il comando /start
    updater.dispatcher.add_handler(CommandHandler("start", start))

    # Avvia il bot
    print("Il bot è in esecuzione...")
    updater.start_polling()

    # Mantieni il bot attivo
    updater.idle()

if __name__ == "__main__":
    main()



