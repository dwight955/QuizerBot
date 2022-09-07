
from controller.handler.handler_command import UserContext
from main import *
from generalVariable.variable import Variable
from controller.handler.gameFinish import finishGame

async def receive_quiz_answer(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Close quiz after three participants took it"""
    # print(update.poll.options[3].voter_count)
    global save_event_game

    if update.poll.options[3].voter_count >= 1:
        Variable.answer_complete["puntos"] += 5
        if Variable.answer_complete["complete"] <= 0:
            Variable.answer_complete["complete"] = 1
            await poll(UserContext.save_event_game[0], UserContext.save_event_game[1])
        elif Variable.answer_complete["complete"] == 1:
            await finishGame(update, context)
            
        # elif answer_complete["complete"] >= 2:
    else:
        if Variable.answer_complete["complete"] <= 0:
            Variable.answer_complete["complete"] = 1
            print("=======********========")
            print(UserContext.save_event_game)
            await poll(UserContext.save_event_game[0], UserContext.save_event_game[1])
        elif Variable.answer_complete["complete"] == 1:
            await finishGame(update, context)
        # print(answer_complete["complete"])
        

    # print(answer_complete["puntos"])