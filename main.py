import asyncio
import random
from email import message
from glob import glob
from itertools import count
import logging
from multiprocessing.connection import wait
from string import punctuation
from timeit import repeat
from typing import Dict
from telegram import __version__ as TG_VER

from telegram import(
    Poll,
    Update,
)
from telegram.ext import(
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
    PollAnswerHandler,
    PollHandler
)
import config
from quizers import quizers

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
 # variable globals
answer_complete = {"puntos": 0, "complete": 0, "chat_id": 0}
save_event_game = [0, 0]
quiz_old = []
# assign quiz
quiz_actually = random.choice(quizers)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Welcome to the Bot - con nuevo token")

async def poll(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Sends a predefined poll"""
    answer_complete["chat_id"] = update.effective_chat.id
    questions = ["JavaScript","REACT","CSS","HTML"]
    message = await context.bot.send_poll(
        update.effective_chat.id,
        "Cuales son las tecnologia que se utilizan para comenzar a crear una pagina web?",
        questions,
        is_anonymous=False,
        allows_multiple_answers=True,
    )
    global save_event_game
    save_event_game = [update, context]

async def quiz(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a predefined poll"""
    global save_event_game, quiz_old, quiz_actually
    answer_complete["chat_id"] = update.effective_chat.id
    if(len(quizers) > 0):
        message = await update.effective_message.reply_poll(
            quiz_actually["question"],
            quiz_actually["options"], 
            type=Poll.QUIZ,
            correct_option_id=quiz_actually["answer_id"],
            explanation= quiz_actually["answer"]
        )
        quizers.remove(quiz_actually)
        print(quizers)
    else:
        await getQuiz(update, context)
    save_event_game = [update, context]

async def receive_quiz_answer(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Close quiz after three participants took it"""
    # print(update.poll.options[3].voter_count)

    # if update.poll.options[3].voter_count >= 1:
    #     answer_complete["puntos"] += 5
    #     if answer_complete["complete"] <= 0:
    #         answer_complete["complete"] = 1
    #         await quiz(save_event_game[0], save_event_game[1])
    #     elif answer_complete["complete"] == 1:
    #         await finishGame(update, context)
            
    #     # elif answer_complete["complete"] >= 2:
    # else:
    #     if answer_complete["complete"] <= 0:
    #         answer_complete["complete"] = 1
    #         await quiz(save_event_game[0], save_event_game[1])
    #     elif answer_complete["complete"] == 1:
    #         await finishGame(update, context)
        # print(answer_complete["complete"])
    await quiz(save_event_game[0], save_event_game[1])

    # print(answer_complete["puntos"])

async def receive_poll_answer(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Summarize a users poll vote"""
    answer = update.poll_answer
    # print(answer)
    if answer.option_ids == [0,2,3]:
        answer_complete["puntos"] += 5
        if answer_complete["complete"] <= 0:
            answer_complete["complete"] = 1
            await quiz(save_event_game[0], save_event_game[1])
        elif answer_complete["complete"] == 1:
            await finishGame(update, context)
        # elif answer_complete["complete"] >= 2:
        # print("B: " + str(answer_complete["complete"]))
    else:
        # print("A: " + str(answer_complete["complete"]))
        if answer_complete["complete"] <= 0:
            answer_complete["complete"] = 1
            await quiz(save_event_game[0], save_event_game[1])
        elif answer_complete["complete"] == 1:
            await finishGame(update, context)

    # print(answer_complete["puntos"])


async def finishGame(update, context):
    # print("Llego")
    puntos = 0
    mensaje = ""
    if answer_complete['puntos'] == 0:
        mensaje = f"Lo siento obtuviste {answer_complete['puntos']} puntos"
    elif answer_complete['puntos'] == 5:
        mensaje = f"No estuviste tan mal, sacaste {answer_complete['puntos']}/10 puntos"
    elif answer_complete['puntos'] >= 10:
        mensaje = f"Felicidades sacaste {answer_complete['puntos']}/10 puntos"

    await context.bot.send_message(chat_id=answer_complete["chat_id"], text=mensaje)

    # print(answer_complete["complete"])
    answer_complete["complete"] = 0
    answer_complete["puntos"] = 0

async def getQuiz(Update, Context)-> None:
    global quiz_actually
    quiz_actually = random.choice(quizers)
    await quiz(Update, Context)

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # print(update)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)


if __name__ == '__main__':
    application = ApplicationBuilder().token(config.VariableConst.MY_TOKEN_BOT).build()

    application.add_handler(CommandHandler('start',start))
    application.add_handler(CommandHandler('poll', poll))
    application.add_handler(CommandHandler('quiz', quiz))

    application.add_handler(PollHandler(receive_quiz_answer))
    application.add_handler(PollAnswerHandler(receive_poll_answer))
    # application.add_handler(MessageHandler(filters.POLL, receive_poll))
    
    application.run_polling()

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


# {'option_ids': [1, 2], 'user': {'is_bot': False, 'username': 'arabeltz', 'first_name': 'Moor', 'last_name': 'Mood', 'id': 1822798056, 'language_code': 'es'}, 'poll_id': '4952065462285369361'}

# {'total_voter_count': 1, 'allows_multiple_answers': False, 'options': [{'voter_count': 0, 'text': '1800'}, {'voter_count': 0, 'text': '1952'}, {'voter_count': 1, 'text': '1821'}, {'voter_count': 0, 'text': '1921'}], 'type': <PollType.QUIZ>, 'explanation_entities': [], 'is_anonymous': True, 'is_closed': False, 'id': '4952065462285369362', 'explanation': '1821', 'question': 'En que año es la indepencia del Perú?', 'correct_option_id': 2, 'close_date': None}
 