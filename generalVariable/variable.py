from telegram import Update
from telegram.ext import ContextTypes
class Variable:
    currentContext = {
        "typeGame": "poll",
        "update": Update,
        "context": ContextTypes.DEFAULT_TYPE,
        "chat_id": 0,
        "game_id": 0
    }
    gameData = {
        "points": 0,
        "reward": [],
        "gamePlayed": {"poll": 4, "quiz": 0}
    }
# print("Reward: " + str(Variable.dataGame["reward"]))
async def setCurrentContext(typeGame, update, context, chat_id, game_id, dict):
    dict["typeGame"] = typeGame
    dict["update"] = update
    dict["context"] = context
    dict["chat_id"] = chat_id
    dict["game_id"] = game_id

    # print(Variable.currentContext["update"])
