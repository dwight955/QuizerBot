
#1822798056
from controller.handler.handler_command import UserContext
from generalVariable.variable import Variable
from main import *
from game.questions.question_poll import question_game_quiz

async def poll(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Sends a predefined poll"""
    whatQuestion = 0

    message = await context.bot.send_poll(
        update.effective_chat.id,
        question_game_quiz[whatQuestion]["questionTitle"],
        question_game_quiz[whatQuestion]["questionOption"],
        is_anonymous=question_game_quiz[whatQuestion]["voteAnonymous"],
        allows_multiple_answers=question_game_quiz[whatQuestion]["allowsMultipleAnswers"],
    )
    # # global save_event_game
    # UserContext.save_event_game = [update, context]
