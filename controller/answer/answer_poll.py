
from game.quiz import quiz
from controller.handler.handler_command import UserContext
from game.questions.question_poll import question_game_poll
from game.questions.question_quiz import question_game_quiz
from generalVariable.variable import Variable
from main import *
import random
async def receive_poll_answer(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Summarize a users poll vote"""
    answer = update.poll_answer

    current_data = Variable.currentContext
    game_data = Variable.gameData
    #increase count gaem


    if current_data["typeGame"] == "poll":
        Variable.gameData["gamePlayed"]["poll"] = (Variable.gameData["gamePlayed"]["poll"]) + 1
        reward_game = ["🎁", "✨", "🐱", "👤", "🎶", "🌹", "💖", "‍🏍", "‍👓", "‍🚀", "‍🐉", "👏", "👍", "👌", "💕"]
        correct_answer = question_game_poll[current_data["game_id"]]["correct_answer"]

        if answer.option_ids == correct_answer:
            game_data["points"] += 5
            game_data["reward"].append(reward_game[random.randint(0, len(reward_game)-1)])

            print(f"La respuesta: {answer.option_ids} & {correct_answer}, son iguales")



    # chat_id = answer.user.id
    # correctAnswer = answer.option_ids
    print(game_data)

    #answer.option_ids = Option selected by the user
    #await finishGame(update, context) Game finished
