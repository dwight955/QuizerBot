from controller.handler.gameFinish import finishGame
from game.database.dbData import get_user_data
from game.database.userId import set_user_data_id
from game.questions.question_poll import question_game_poll
from main import *


async def poll(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    id_user = update.message.chat.id
    # Variable que se encarga de almacenar todos los datos del usuario
    user_data = get_user_data(id_user)
    # Variable para obtener el numero de pregunta respondida actual
    poll_answered = user_data["polls_answered"]

    set_user_data_id(str(update.message.chat.id)[0:7], 'id', update.message.chat.id)

    keyboard = [
        [
            InlineKeyboardButton("\u274C", callback_data="finish-poll"),
            InlineKeyboardButton("\u27A1", callback_data="next-poll"),
        ],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    if poll_answered <= (len(question_game_poll)-1):
        message = await context.bot.send_poll(
            update.message.chat.id,
            question_game_poll[poll_answered]["question"],
            question_game_poll[poll_answered]["options"],
            is_anonymous=question_game_poll[poll_answered]["voteAnonymous"],
            allows_multiple_answers=question_game_poll[poll_answered]["allowsMultipleAnswers"],
            open_period=10,
            reply_markup=reply_markup,
        )
    else:
        if not (await finishGame(context, id_user)):
            await context.bot.send_message(update.message.chat.id,
                                           "Lo sentimos ya no hay mas preguntas!\n\nPuede jugar el otro juego\n\n /quiz")