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
    # print(update.callback_query.message.poll)

    """El answer_option, devuelve el valor que el usuario selecciono, 
       esta puede ser tanto 'quiz', 'random' o 'poll'"""
    # Condicional para enviar un quiz, cuando el callback que se reciba sera 'quiz'

    await update.callback_query.edit_message_reply_markup(reply_markup=InlineKeyboardMarkup([[]]))

    match answer_option:
        case 'next-quiz':
            answers_dude = [y['voter_count'] for y in update.callback_query.message.poll.options]
            if str(answers_dude).find("1") == -1:
                save_data(id_user, "questions_answered", "quizs_answered")

            user_data = get_user_data(id_user)
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
            else:
                await context.bot.send_message(id_user,
                                               "Lo sentimos ya no hay mas preguntas!\n\nPuede jugar el otro juego\n\n /quiz")
        case 'next-poll':
            answers_dude = [y['voter_count'] for y in update.callback_query.message.poll.options]
            if str(answers_dude).find("1") == -1:
                save_data(id_user, "questions_answered", "polls_answered")

            user_data = get_user_data(id_user)

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
            else:
                await context.bot.send_message(id_user,
                                   "Lo sentimos ya no hay mas preguntas!\n\nPuede jugar el otro juego\n\n /poll")

    if answer_option in ('finish-poll', 'finish-quiz'):
        result = 'Resultado'.center(50, '-')
        text = f'*{result}*\n\nCant. de pregunta respondida: *{user_data["questions_answered"]}/{len_question_total}*\n' \
               f'Cant. de quiz: *{user_data["quizs_answered"]}/{len_question_quiz}*\nCant. de poll: *{user_data["polls_answered"]}/{len_question_poll}*\n' \
               f'Puntuación total: *{user_data["points"]}*'
        await context.bot.send_message(chat_id=id_user, text=text, parse_mode='Markdown')
