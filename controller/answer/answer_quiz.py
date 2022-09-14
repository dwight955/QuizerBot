
from controller.handler.handler_command import UserContext
from main import *
from game import quiz
from generalVariable.variable import (Variable)
from controller.handler.gameFinish import finishGame
from game.questions.question_quiz import question_game_quiz
from game.database.dbReward import (save_user, data_save)
from game.database.dbData import (get_user_data, set_user_data)
import random

async def receive_quiz_answer(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Close quiz after three participants took it"""
    answer = update
    # Indicador de que el usuario respondio
    Variable.is_request = True
    current_data = Variable.currentContext
    game_data = Variable.gameData
    #increase count gaem

    if current_data["typeGame"] == "quiz":
        Variable.gameData["gamePlayed"]["quiz"] += 1

        dict_get_data_user = (get_user_data(current_data["chat_id"]))
        count_questions_answered = dict_get_data_user["questions_answered"] + 1
        # print(count_questions_answered)
        set_user_data(current_data["chat_id"], "questions_answered", count_questions_answered)

        # reward_game = ["🧶", "🎄", "🎎", "🎫", "🎟", "🎨", "🥽", "‍🎭", "‍🎪", "‍🎃", "‍👕", "🎑", "💎", "⚽", "🏀"]
        reward_game = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
        correct_answer = question_game_quiz[current_data["game_id"]]["index_correct_answer"]

        if answer.poll.options[correct_answer]["voter_count"] == 1:
            game_data["points"] += 5
            count_win_points = dict_get_data_user["points"] + 5
            set_user_data(current_data["chat_id"], "points", count_win_points)

            game_data["reward"].append(reward_game[random.randint(0, len(reward_game)-1)])

            reward = reward_game[random.randint(0, len(reward_game)-1)]
            game_data["reward"].append(reward)

            if (await save_user(current_data["chat_id"])):
                await data_save(reward, current_data["chat_id"])
            else:
                await data_save(reward, current_data["chat_id"])

            print(f"La respuesta: {answer.poll.options[correct_answer]['voter_count']} & 1, son iguales")
    # Se espera que el hilo t1 termine
    quiz.t1.join()
    # Se asegura que el Hilo t1 este muerto
    if(quiz.t1.is_alive()!=True):
        # Se envia el siguiente quiz
        await quiz.quiz(Variable.currentContext["update"], Variable.currentContext["context"])
    print(game_data)

    #answer.option_ids = Option selected by the user
    #await finishGame(update, context) Game finished

