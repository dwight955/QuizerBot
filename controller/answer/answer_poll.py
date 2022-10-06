from game.questions.question_poll import question_game_poll
from game.database.dbReward import data_save
from main import *
import random
from game.database.dbData import set_user_data, save_data

async def receive_poll_answer(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Summarize a users poll vote"""
    answer = update.poll_answer
    id_user = answer.user.id

    dict_get_data_user = save_data(id_user, "questions_answered", "polls_answered")

    reward_game = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]

    correct_answer = question_game_poll[dict_get_data_user["quizs_answered"]]["index_correct_answer"]

    if answer.option_ids == correct_answer:
        count_win_points = dict_get_data_user["points"] + 5
        set_user_data(id_user, "points", count_win_points)

    reward = reward_game[random.randint(0, len(reward_game) - 1)]
    await data_save(reward, id_user)
