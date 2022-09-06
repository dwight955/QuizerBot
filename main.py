import asyncio
import logging
from telegram import __version__ as TG_VER

from telegram import(
    Poll,
    Update
)
from telegram.ext import(
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
    PollAnswerHandler,
    PollHandler,
)
import config

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Welcome to the Bot :) ")

if __name__ == '__main__':
    application = ApplicationBuilder().token(config.VariableConst.MY_TOKEN_BOT).build()

    application.add_handler(CommandHandler('start',start))

    application.run_polling()

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
