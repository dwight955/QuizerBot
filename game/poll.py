
#1822798056
from controller.handler.handler_command import UserContext
from generalVariable.variable import (Variable, setCurrentContext)
from main import *
from game.questions.question_poll import question_game_poll

async def poll(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Sends a predefined poll"""
    whatQuestion = Variable.gameData["gamePlayed"]["poll"]

    if Variable.gameData["gamePlayed"]["poll"] <= (len(question_game_poll)-1):
        message = await context.bot.send_poll(
            update.effective_chat.id,
            question_game_poll[whatQuestion]["question"],
            question_game_poll[whatQuestion]["options"],
            is_anonymous=question_game_poll[whatQuestion]["voteAnonymous"],
            allows_multiple_answers=question_game_poll[whatQuestion]["allowsMultipleAnswers"],
        )
    else:
        await context.bot.send_message(update.effective_chat.id,
                                       "Lo sentimos ya no hay mas preguntas!\n\nPuede jugar el otro juego\n\n /quiz")

    # print(Variable.dataGame["gamePlayed"])
    await setCurrentContext("poll", update, context, update.effective_chat.id, whatQuestion, Variable.currentContext)

    # # global save_event_game
    # UserContext.save_event_game = [update, context]
