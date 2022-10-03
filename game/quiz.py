import asyncio
from main import *
from game.questions.question_quiz import question_game_quiz
from game.database.dbData import get_user_data
from game.database.userId import set_user_data_id

async def quiz(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a predefined poll"""

    # Variable que se encarga de almacenar todos los datos del usuario
    user_data = get_user_data(update.message.chat.id)
    # Variable para obtener el numero de pregunta respondida actual
    quiz_answered = user_data["quizs_answered"]

    set_user_data_id(str(update.message.chat.id)[0:7], 'id', update.message.chat.id)

    if quiz_answered <= (len(question_game_quiz) - 1):
        keyboard = [
            [
                InlineKeyboardButton("Quiz", callback_data="quiz"),
                InlineKeyboardButton("Random", callback_data="random"),
                InlineKeyboardButton("Poll", callback_data="poll"),
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
        await context.bot.send_message(update.message.chat.id,
                                       "Lo sentimos ya no hay mas preguntas!\n\nPuede jugar el otro juego\n\n /poll")

