
from main import *

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # print(update)

    await context.bot.send_message(chat_id=update.message.chat.id, text=update.message.text)
