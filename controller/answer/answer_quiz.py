
from controller.handler.handler_command import UserContext
from main import *
from generalVariable.variable import Variable
from controller.handler.gameFinish import finishGame

async def receive_quiz_answer(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Close quiz after three participants took it"""
    answer = update.poll_answer

    #answer.option_ids = Option selected by the user
    #await finishGame(update, context) Game finished

