from main import *
from game.quiz import quiz
from game.poll import poll
from game.database.dbData import *
from generalVariable.variable import len_question_quiz, len_question_poll, len_question_total
from game import poll, quiz

num_random: int = 0

async def receive_inline_keyboard(update: Update, context:ContextTypes.DEFAULT_TYPE) -> None:
    answer = update.callback_query
    answer_option = answer.data
    id_user = answer.message.chat.id
    # Variable que se encarga de almacenar todos los datos del usuario
    user_data = get_user_data(id_user)

    """El answer_option, devuelve el valor que el usuario selecciono, 
       esta puede ser tanto 'quiz', 'random' o 'poll'"""
    # Condicional para enviar un quiz, cuando el callback que se reciba sera 'quiz'
<<<<<<< HEAD

    await update.callback_query.edit_message_reply_markup(reply_markup=InlineKeyboardMarkup([[]]))

    match answer_option:
        case 'next-quiz':
            save_data(id_user, "questions_answered", "quizs_answered")

            # Variable para obtener el numero de pregunta respondida actual
            quiz_answered = user_data["quizs_answered"]

            quiz.set_user_data_id(str(id_user)[0:7], 'id', id_user)

            if quiz_answered <= (len(quiz.question_game_quiz) - 1):
                keyboard = [
                    [
                        InlineKeyboardButton("\u274C", callback_data="finish-quiz"),
                        InlineKeyboardButton("\u27A1", callback_data="next-quiz"),
                    ],
                ]

                reply_markup = InlineKeyboardMarkup(keyboard)

                message = await update.callback_query.message.reply_poll(
                    quiz.question_game_quiz[quiz_answered]["question"],
                    quiz.question_game_quiz[quiz_answered]["options"],
                    type=Poll.QUIZ,
                    correct_option_id=quiz.question_game_quiz[quiz_answered]["index_correct_answer"],
                    explanation=quiz.question_game_quiz[quiz_answered]["explanation"] + " \n#" + str(id_user)[0:7],
                    open_period=10,
                    reply_markup=reply_markup,

                )
        case 'next-poll':
            save_data(id_user, "questions_answered", "polls_answered")
            # Variable que se encarga de almacenar todos los datos del usuario
            # Variable para obtener el numero de pregunta respondida actual
            poll_answered = user_data["polls_answered"]

            poll.set_user_data_id(str(id_user)[0:7], 'id', id_user)

            keyboard = [
                [
                    InlineKeyboardButton("\u274C", callback_data="finish-poll"),
                    InlineKeyboardButton("\u27A1", callback_data="next-poll"),
                ],
            ]

            reply_markup = InlineKeyboardMarkup(keyboard)

            if poll_answered <= (len(poll.question_game_poll) - 1):
                message = await context.bot.send_poll(
                    id_user,
                    poll.question_game_poll[poll_answered]["question"],
                    poll.question_game_poll[poll_answered]["options"],
                    is_anonymous=poll.question_game_poll[poll_answered]["voteAnonymous"],
                    allows_multiple_answers=poll.question_game_poll[poll_answered]["allowsMultipleAnswers"],
                    open_period=10,
                    reply_markup=reply_markup,
                )

    if answer_option.index('finish') != -1:
        result = 'Resultado'.center(50, '-')
        text = f'*{result}*\n\nCant. de pregunta respondida: *{user_data["questions_answered"]}/{len_question_total}*\n' \
               f'Cant. de quiz: *{user_data["quizs_answered"]}/{len_question_quiz}*\nCant. de poll: *{user_data["polls_answered"]}/{len_question_poll}*\n' \
               f'Puntuación total: *{user_data["points"]}*'
        await context.bot.send_message(chat_id=id_user, text=text, parse_mode='Markdown')
=======
    if answer_option == 'quiz':
        await quiz(update=answer, context=context)

    elif answer_option == 'random':
        # En esta condicional se verifica el numero de preguntas respondida por el usuario, y si tanto
        # en el poll o quiz, es menor que el total de preguntas a responder, entonces se selecciona de
        # manera aleatoria una pregunta del poll o quiz
        if (user_data["polls_answered"] < len(question_poll.question_game_poll) and user_data["quizs_answered"] < len(question_quiz.question_game_quiz)):
        # num_random se encarga de generar un numero del 0 a 1
            num_random = random.randint(0, 1)
        elif user_data["polls_answered"] < len(question_poll.question_game_poll):
            # si la condicion entra aqui la variable random_question  se encargara de
            # seleccionar la funcion de la lista [quiz, poll] en el index 1, que corresponde
            # a la funcion poll.
            num_random = 1
        # random_question es una lista donde se almacena las funciones,
        # para luego ser llamada aleatoriamente
        # Codigo que se encarga de llamar la funcion para enviarle
        # al usuario ya sea un quiz o poll
        await random_question[num_random](answer, context)

    # Condicional para enviar un quiz, cuando el callback que se reciba sera 'poll'
    elif answer_option == 'poll':
        await poll(update=answer, context=context)
>>>>>>> 81b881fc0f99544512e50dab131fb337f27be57e

    # Para poder editar el mensaje que le enviamos y asi lograr eliminar los botones
    # para evitar que pueda pulsar el Boton de nuevo.
    # await answer.edit_message_reply_markup(reply_markup=InlineKeyboardMarkup([]))
