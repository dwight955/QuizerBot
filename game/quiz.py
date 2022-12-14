import asyncio

from controller.handler.gameFinish import finishGame
from main import *
from game.questions.question_quiz import question_game_quiz
from game.database.dbData import get_user_data
from game.database.userId import set_user_data_id

async def quiz(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    id_user = update.message.chat.id
    # Variable que se encarga de almacenar todos los datos del usuario
    user_data = get_user_data(id_user)
    # Variable para obtener el numero de pregunta respondida actual
    quiz_answered = user_data["quizs_answered"]

    set_user_data_id(str(update.message.chat.id)[0:7], 'id', update.message.chat.id)

    if quiz_answered <= (len(question_game_quiz) - 1):

        keyboard = [
            [
                InlineKeyboardButton("\u274C", callback_data="finish-quiz"),
                InlineKeyboardButton("\u27A1", callback_data="next-quiz"),
            ],
        ]

        reply_markup = InlineKeyboardMarkup(keyboard)

        message = await update.message.reply_poll(
            question_game_quiz[quiz_answered]["question"],
            question_game_quiz[quiz_answered]["options"],
            type=Poll.QUIZ,
            correct_option_id=question_game_quiz[quiz_answered]["index_correct_answer"],
            explanation=question_game_quiz[quiz_answered]["explanation"] + " \n#" + str(update.message.chat.id)[0:7],
            open_period=10,
            reply_markup=reply_markup,

        )
    else:
        if not (await finishGame(context, id_user)):
            await context.bot.send_message(update.message.chat.id,
                                        "Lo sentimos ya no hay mas preguntas!\n\nPuede jugar el otro juego\n\n /poll")

