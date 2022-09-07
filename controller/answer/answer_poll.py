
from game.quiz import quiz
from controller.handler.handler_command import UserContext
from main import *
from generalVariable.variable import Variable

async def receive_poll_answer(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Summarize a users poll vote"""
    answer = update.poll_answer
    global save_event_game
    print("A: ============" + str(UserContext.save_event_game))

    # print(answer)
    if answer.option_ids == [0,2,3]:
        Variable.answer_complete["puntos"] += 5
        if Variable.answer_complete["complete"] <= 0:
            Variable.answer_complete["complete"] = 1
            await quiz(UserContext.save_event_game[0], UserContext.save_event_game[1])
        elif Variable.answer_complete["complete"] == 1:
            await finishGame(update, context)
        # elif answer_complete["complete"] >= 2:
        # print("B: " + str(answer_complete["complete"]))
    else:
        # print("A: " + str(answer_complete["complete"]))
        if Variable.answer_complete["complete"] <= 0:
            Variable.answer_complete["complete"] = 1
            await quiz(UserContext.save_event_game[0], UserContext.save_event_game[1])
        elif Variable.answer_complete["complete"] == 1:
            await finishGame(update, context)
        

    # print(answer_complete["puntos"])
