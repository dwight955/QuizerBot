
from game.quiz import quiz
from controller.handler.handler_command import UserContext
from game.questions.question_poll import question_game_poll
from game.questions.question_quiz import question_game_quiz
from generalVariable.variable import Variable
from game.database.dbReward import (save_user, data_save)
from main import *
import random
from game.database.dbData import (get_user_data, set_user_data)


async def receive_poll_answer(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Summarize a users poll vote"""
    answer = update.poll_answer

    current_data = Variable.currentContext
    game_data = Variable.gameData
    #increase count gaem
    if current_data["typeGame"] == "poll":
        Variable.gameData["gamePlayed"]["poll"] += 1
        dict_get_data_user = (get_user_data(current_data["chat_id"]))
        count_questions_answered = dict_get_data_user["questions_answered"] + 1
        count_polls_answered = dict_get_data_user["polls_answered"] + 1
        data_to_modify = {
            "questions_answered": count_questions_answered,
            "polls_answered": count_polls_answered
        }
        # print(count_questions_answered)
        set_user_data(current_data["chat_id"], data_to_modify, count_questions_answered)
        # none_user_data = set_user_data(current_data["chat_id"], "points", 10)


        # reward_game = ["🎁", "✨", "🐱", "👤", "🎶", "🌹", "💖", "‍🏍", "‍👓", "‍🚀", "‍🐉", "👏", "👍", "👌", "💕"]
        reward_game = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]

        correct_answer = question_game_poll[current_data["game_id"]]["index_correct_answer"]

        if answer.option_ids == correct_answer:
            # game_data["points"] += 5
            count_win_points = dict_get_data_user["points"] + 5
            set_user_data(current_data["chat_id"], "points", count_win_points)

            reward = reward_game[random.randint(0, len(reward_game)-1)]
            game_data["reward"].append(reward)
            await data_save(reward, current_data["chat_id"])

            # print(f"La respuesta: {answer.option_ids} & {correct_answer}, son iguales")

    # chat_id = answer.user.id
    # correctAnswer = answer.option_ids
    # print(game_data)

    #answer.option_ids = Option selected by the user
    #await finishGame(update, context) Game finished
