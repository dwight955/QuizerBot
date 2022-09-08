from telegram import Update
from telegram.ext import ContextTypes
class Variable:
    currentContext = {
        "typeGame": "pool",
        "update": Update,
        "context": ContextTypes.DEFAULT_TYPE,
        "chat_id": 0
    }