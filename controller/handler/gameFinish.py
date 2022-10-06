from generalVariable.constant import CONSTANT
from main import *
from game.database import dbData
from game.questions import question_poll, question_quiz

async def finishGame(update, context, id):
    data_finish = dbData.get_user_data(id)
    # Total de puntos obtenidos
    total_points = data_finish["points"]
    # Total de polls respondidas
    total_polls_answered = data_finish["polls_answered"]
    # Total de quiz respondidas
    total_quiz_answered = data_finish["quizs_answered"]
    # Si el total de respondidas es igual al total de polls y quiz
    if total_polls_answered == (len(question_poll.question_game_poll)-1 and
                                total_quiz_answered == (len(question_quiz.question_game_quiz)-1)):
        mensaje = (
            "*--- FIN DEL JUEGO ---*\n"
            "¡Muchas Gracias por jugar!\n"
            f"Tu puntuacion final: *{total_points}*\n"
            f"Cantidad de Polls respondidas : *{total_polls_answered}*\n"
            f"Cantidad de Quiz respondidas : *{total_quiz_answered}*"
        )
    await context.bot.send_message(chat_id=update.message.chat_id, text=mensaje, parse_mode="Markdown")