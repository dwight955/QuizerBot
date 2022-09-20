import threading

from telegram import Update
from telegram.ext import ContextTypes
from threading import Timer
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
        "gamePlayed": {
            "poll": 0,
            "quiz": 0
        }
    }
    is_request = False
    timer = threading
# print("Reward: " + str(Variable.dataGame["reward"]))
async def set_current_context(typeGame, update, context, chat_id, dict):
    dict["typeGame"] = typeGame
    dict["update"] = update
    dict["context"] = context
    dict["chat_id"] = chat_id
    Variable().currentContext["chat_id"] = dict["chat_id"]

    # print(Variable.currentContext["update"])
