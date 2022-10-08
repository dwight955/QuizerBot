from generalVariable.constant import CONSTANT
from main import *
from game.database import dbData, dbReward
from generalVariable import variable, constant

async def finishGame(context, id) -> bool:
    data_finish = dbData.get_user_data(id)
    # Total de puntos obtenidos
    get_total_points = data_finish["points"]
    # Total de polls respondidas
    total_polls_answered = data_finish["polls_answered"]
    # Total de quiz respondidas
    total_quiz_answered = data_finish["quizs_answered"]
    # Si el total de respondidas es igual al total de polls y quiz
    if total_polls_answered == (variable.len_question_poll) and total_quiz_answered == (variable.len_question_quiz):
        # Total de puntos
        total_points = variable.len_question_total * CONSTANT.GIVE_POINTS
        # Porcentaje obtenido de la puntuacion total
        percentage_points = (get_total_points * 100) / total_points
        # Mensaje final basado en el porcentaje de puntos total
        msg_final = ""
        if(percentage_points < 25):
            msg_final = "¡Esfuerzate más!"
        elif(percentage_points >= 25 and percentage_points <= 55):
            msg_final = "No estuvo mal"
        elif (percentage_points > 55 and percentage_points <= 80):
            msg_final = "Estuviste genial"
        elif (percentage_points > 80 and percentage_points <= 90):
            msg_final = "¡Maravillosa jugada!"
        else:
            msg_final = "¡GENIAL! Eres lo maximo"

        rewards = dbReward.get_user_reward(id)
        sRewards = str(rewards).replace("'", "")

        mensaje = (
            "* FIN DEL JUEGO *".center(50, '-') +
            "\n\n¡Muchas Gracias por jugar!\n"
            f"Tu puntuacion final: *{get_total_points}*\n"
            f"Cantidad de Polls respondidas : *{total_polls_answered}*\n"
            f"Cantidad de Quiz respondidas : *{total_quiz_answered}*\n"
            f"Porcetaje de presicion : *{percentage_points}*%\n"
            f"Cantidad de recompensas obtenidas : \n{sRewards}\n\n"
            f"{msg_final}"
        )
        await context.bot.send_message(id, text=mensaje, parse_mode="Markdown")
        return True