from game.questions.question_poll import question_game_poll
from game.database.dbReward import data_save
from generalVariable.constant import *
from main import *
import random
from game.database.dbData import (get_user_data, set_user_data)

async def receive_poll_answer(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Summarize a users poll vote"""
    answer = update.poll_answer
    id_user = answer.user.id

    dict_get_data_user = (get_user_data(id_user=id_user))

    count_questions_answered = dict_get_data_user["questions_answered"] + 1
    count_polls_answered = dict_get_data_user["polls_answered"] + 1

    data_to_modify = {
    "questions_answered": count_questions_answered,
    "polls_answered": count_polls_answered,
    }

    set_user_data(id_user, data_to_modify, 0)

    reward_game = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]

    correct_answer = question_game_poll[dict_get_data_user["quizs_answered"]]["index_correct_answer"]

    if answer.option_ids == correct_answer:
        count_win_points = dict_get_data_user["points"] + CONSTANT.GIVE_POINTS
        set_user_data(id_user, "points", count_win_points)

    reward = reward_game[random.randint(0, len(reward_game) - 1)]
    await data_save(reward, id_user)
