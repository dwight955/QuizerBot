
from controller.handler.handler_command import UserContext
from main import *
from generalVariable.variable import (Variable, setCurrentContext)
from game.questions.question_quiz import question_game_quiz
from generalVariable.constant import CONSTANT
import time

async def quiz(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a predefined poll"""
    whatQuestion = Variable.gameData["gamePlayed"]["quiz"]
    if Variable.gameData["gamePlayed"]["quiz"] <= (len(question_game_quiz)-1):
        # questions = ["24 DE ENERO DE 1844", "04 DE ENERO DE 1834", "27 DE MAYO DEL 1846", "27 DE FEBRERO DE 1844"]

        message = await update.effective_message.reply_poll(
            question_game_quiz[whatQuestion]["question"],
            question_game_quiz[whatQuestion]["options"],
            type=Poll.QUIZ,
            correct_option_id=question_game_quiz[whatQuestion]["index_correct_answer"],
            explanation=question_game_quiz[whatQuestion]["explanation"],
            open_period=10,
            pool_timeout=5000
        )
    else:
        await context.bot.send_message(update.effective_chat.id,
                                       "Lo sentimos ya no hay mas preguntas!\n\nPuede jugar el otro juego\n\n /poll")
    await setCurrentContext("quiz", update, context, update.message.chat.id, whatQuestion, Variable.currentContext)

