from main import *
from game.quiz import *
from game.questions.question_quiz import question_game_quiz
from game.database.dbReward import data_save
from game.database.dbData import (get_user_data, set_user_data)
import random
from generalVariable.constant import *
from game.database.userId import get_user_id
async def receive_quiz_answer(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Close quiz after three participants took it"""
    answer = update

    user_id = get_user_id(update.poll.explanation[-7:])

    dict_get_data_user = (get_user_data(user_id))
    count_questions_answered = dict_get_data_user["questions_answered"] + 1
    count_quizs_answered = dict_get_data_user["quizs_answered"] + 1

    data_to_modify = {
        "questions_answered": count_questions_answered,
        "quizs_answered": count_quizs_answered
    }

    set_user_data(user_id, data_to_modify, count_questions_answered)

    reward_game = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]

    correct_answer = question_game_quiz[dict_get_data_user["quizs_answered"]]["index_correct_answer"]

    if answer.poll.options[correct_answer]["voter_count"] == 1:
        count_win_points = dict_get_data_user["points"] + CONSTANT.GIVE_POINTS
        set_user_data(user_id, "points", count_win_points)

        reward = reward_game[random.randint(0, len(reward_game) - 1)]
        await data_save(reward, user_id)


