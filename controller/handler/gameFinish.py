
from main import *
from generalVariable.variable import Variable

async def finishGame(update, context):
    # print("Llego")
    puntos = 0
    mensaje = ""
    if Variable.answer_complete['puntos'] == 0:
        mensaje = f"Lo siento obtuviste {Variable.answer_complete['puntos']} puntos"
    elif Variable.answer_complete['puntos'] == 5:
        mensaje = f"No estuviste tan mal, sacaste {Variable.answer_complete['puntos']}/10 puntos"
    elif Variable.answer_complete['puntos'] >= 10:
        mensaje = f"Felicidades sacaste {Variable.answer_complete['puntos']}/10 puntos"

    await context.bot.send_message(chat_id=Variable.answer_complete["chat_id"], text=mensaje)

    # print(answer_complete["complete"])
    Variable.answer_complete["complete"] = 0
    Variable.answer_complete["puntos"] = 0
