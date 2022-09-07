
from game.quiz import quiz
from controller.handler.handler_command import UserContext
from generalVariable.variable import Variable
from main import *
async def receive_poll_answer(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Summarize a users poll vote"""
    answer = update.poll_answer

    #answer.option_ids = Option selected by the user
    #await finishGame(update, context) Game finished

