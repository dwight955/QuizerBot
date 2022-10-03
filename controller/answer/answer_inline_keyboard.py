from main import *
import random
from game.quiz import quiz
from game.poll import poll
from game.database.dbData import *
from game.questions import question_poll, question_quiz


num_random: int = 0

async def receive_inline_keyboard(update: Update, context:ContextTypes.DEFAULT_TYPE) -> None:
    answer = update.callback_query
    answer_option = answer.data
    global num_random
    # print(update)
    """ 
    En esta 'user_data' variable se llama la funcion 'get_user_data' la cual devolvera un diccionario
    con la siguiente estructura:
    dict_data = {
        "questions_answered": None, # Corresponde al total de preguntas respondida (int)
        "points": None, # Los puntos acumulado hasta el momento (int)
        "polls_answered": None, # EL total de preguntas respondida en el Poll (int)
        "quizs_answered": None # EL total de preguntas respondida en el Quiz (int)
    }
    """
    user_data = get_user_data(answer.message.chat.id)

    # Lista donde se almacena las dos funciones, para ser seleccionada
    # aleatoriamente.
    random_question = [quiz, poll]
    # por defecto se mandara a llamar al juego quiz, siemrpe y cuando las
    # condicionales que estan abajo, sean falsa.

    """El answer_option, devuelve el valor que el usuario selecciono, 
       esta puede ser tanto 'quiz', 'random' o 'poll'"""
    # Condicional para enviar un quiz, cuando el callback que se reciba sera 'quiz'
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

    # Para poder editar el mensaje que le enviamos y asi lograr eliminar los botones
    # para evitar que pueda pulsar el Boton de nuevo.
    # await answer.edit_message_reply_markup(reply_markup=InlineKeyboardMarkup([]))
