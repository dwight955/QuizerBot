from main import *
from game.quiz import *
from game.questions.question_quiz import question_game_quiz
from game.database.dbReward import data_save
from game.database.dbData import set_user_data, save_data
import random
from generalVariable.constant import *
from game.database.userId import get_user_id
async def receive_quiz_answer(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Close quiz after three participants took it"""
    answer = update

    id_user = get_user_id(update.poll.explanation[-7:])

    dict_get_data_user = save_data(id_user, "questions_answered", "quizs_answered")

    reward_game = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]

    correct_answer = question_game_quiz[dict_get_data_user["quizs_answered"]]["index_correct_answer"]

    if answer.poll.options[correct_answer]["voter_count"] == 1:
        count_win_points = dict_get_data_user["points"] + 5
        set_user_data(id_user, "points", count_win_points)

        reward = reward_game[random.randint(0, len(reward_game) - 1)]
        await data_save(reward, id_user)


