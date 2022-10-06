import logging
from telegram import __version__ as TG_VER
from telegram import (Poll, Update, InlineKeyboardButton, InlineKeyboardMarkup)
from telegram.ext import (ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes, PollAnswerHandler, PollHandler, MessageHandler)
from telegram.ext import filters
import requests

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
# Estados del juego
status_game = {
    "noQuestionsPoll": False, #El poll se quedo sin preguntas -> por default falso
    "noQuestionsQuiz": False, #El quiz se quedo sin preguntas -> por default falso
    "game_finish" : False, # Estado del juego actual, ¿fin del juego? -> por default falso
}

if __name__ == '__main__':
    from controller.handler.handler_command import *

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
