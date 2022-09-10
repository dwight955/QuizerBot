
from controller.handler.handler_command import UserContext
from main import *
from generalVariable.variable import Variable
from controller.handler.gameFinish import finishGame
from game.questions.question_quiz import question_game_quiz
import random

async def receive_quiz_answer(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Close quiz after three participants took it"""
    answer = update

    current_data = Variable.currentContext
    game_data = Variable.gameData
    #increase count gaem

    if current_data["typeGame"] == "quiz":
        Variable.gameData["gamePlayed"]["quiz"] += 1
        reward_game = ["🧶", "🎄", "🎎", "🎫", "🎟", "🎨", "🥽", "‍🎭", "‍🎪", "‍🎃", "‍👕", "🎑", "💎", "⚽", "🏀"]
        correct_answer = question_game_quiz[current_data["game_id"]]["index_correct_answer"]

        if answer.poll.options[correct_answer]["voter_count"] == 1:
            game_data["points"] += 5
            game_data["reward"].append(reward_game[random.randint(0, len(reward_game)-1)])

            print(f"La respuesta: {answer.poll.options[correct_answer]['voter_count']} & 1, son iguales")


    print(game_data)

    #answer.option_ids = Option selected by the user
    #await finishGame(update, context) Game finished

