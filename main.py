import asyncio
from email import message
from glob import glob
from itertools import count
import logging
from multiprocessing.connection import wait
from string import punctuation
from timeit import repeat
from telegram import __version__ as TG_VER

from telegram import(
    Poll,
    Update
)
from telegram.ext import(
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
    PollAnswerHandler,
    PollHandler
)
import config

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
 # dictionary from context
ctx_quiz_poll ={
    "update": Update,
    "context": ContextTypes.DEFAULT_TYPE
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Welcome to the Bot - con nuevo token")

async def poll(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Sends a predefined poll"""
    questions = ["Good", "Really good", "Fantastic", "Great"]
    message = await context.bot.send_poll(
        update.effective_chat.id,
        "How are you?",
        questions,
        is_anonymous=False,
        allows_multiple_answers=True,
    )
    # save context
    ctx_quiz_poll["update"] = update
    ctx_quiz_poll["context"] = context

async def quiz(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a predefined poll"""
    opt = ["1800", "1952", "1821", "1921"]
    message = await update.effective_message.reply_poll(
                "En que año es la indepencia del Perú?", 
                opt, 
                type=Poll.QUIZ, 
                correct_option_id=2,
                explanation= "1821"
            )
    data_poll = {
        "id_poll": message.poll.id,
        "correct_option_id": message.poll.correct_option_id,
        "options": message.poll.options
    }
    # save context
    ctx_quiz_poll["update"] = update
    ctx_quiz_poll["context"] = context
    context.bot_data.update(data_poll)

async def receive_quiz_answer(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Close quiz after three participants took it"""
    """ for x in update.poll.options:
        print(x) """
    await quiz( ctx_quiz_poll["update"], ctx_quiz_poll["context"])
    # print(update)
    
async def receive_poll_answer(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Summarize a users poll vote"""
    await poll( ctx_quiz_poll["update"], ctx_quiz_poll["context"])

if __name__ == '__main__':
    application = ApplicationBuilder().token(config.VariableConst.MY_TOKEN_BOT).build()

    application.add_handler(CommandHandler('start',start))
    application.add_handler(CommandHandler('poll', poll))
    application.add_handler(CommandHandler('quiz', quiz))

    application.add_handler(PollHandler(receive_quiz_answer))
    application.add_handler(PollAnswerHandler(receive_poll_answer))
    # application.add_handler(MessageHandler(filters.POLL, receive_poll))
    
    application.run_polling()


# {'option_ids': [1, 2], 'user': {'is_bot': False, 'username': 'arabeltz', 'first_name': 'Moor', 'last_name': 'Mood', 'id': 1822798056, 'language_code': 'es'}, 'poll_id': '4952065462285369361'}

# {'total_voter_count': 1, 'allows_multiple_answers': False, 'options': [{'voter_count': 0, 'text': '1800'}, {'voter_count': 0, 'text': '1952'}, {'voter_count': 1, 'text': '1821'}, {'voter_count': 0, 'text': '1921'}], 'type': <PollType.QUIZ>, 'explanation_entities': [], 'is_anonymous': True, 'is_closed': False, 'id': '4952065462285369362', 'explanation': '1821', 'question': 'En que año es la indepencia del Perú?', 'correct_option_id': 2, 'close_date': None}