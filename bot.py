import logging
import os
from dotenv import load_dotenv

from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Завантажуємо змінні середовища з файлу .env
load_dotenv()

# Отримуємо токен з змінної середовища
TOKEN = os.getenv("TOKEN")

if TOKEN is None:
    logging.error("Не знайдено токен бота. Перевірте, чи він прописаний у файлі .env")
    exit()

# Увімкнення логування для відстеження помилок і подій
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

# Функція, що відповідає на команду /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Відповідає на команду /start."""
    await update.message.reply_text('Привіт! Я твій бот. Чим можу допомогти?')

# Функція, що відповідає на текстові повідомлення
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Відповідає на повідомлення користувача."""
    user_text = update.message.text.lower()

    if "привіт" in user_text:
        await update.message.reply_text('Привіт! Радий тебе бачити.')
    elif "як справи" in user_text:
        await update.message.reply_text('Все добре, дякую! Чим цікавишся?')
    elif "що ти вмієш" in user_text:
        await update.message.reply_text('Я вмію відповідати на прості запитання. Спробуй щось запитати!')
    else:
        await update.message.reply_text('Я не знаю відповіді на це питання, вибач.')

def main() -> None:
    """Запускає бота."""
    application = Application.builder().token(TOKEN).build()

    # Додаємо обробники для команд та повідомлень
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Запускаємо бота
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()