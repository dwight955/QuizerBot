
from generalVariable.variable import Variable
from main import *

async def finishGame(update, context):
    mensaje = ""

    await context.bot.send_message(chat_id=Variable.answer_complete["chat_id"], text=mensaje)

