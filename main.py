import asyncio
import logging
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
    PollHandler,
)
import config

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
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

async def quiz(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a predefined poll"""
    questions = ["1800", "1952", "1821", "1921"]
    message = await update.effective_message.reply_poll(
        "En que año es la indepencia del Perú?", 
        questions, 
        type=Poll.QUIZ, 
        correct_option_id=2,
        explanation= "1821"
    )

async def receive_quiz_answer(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Close quiz after three participants took it"""
    print(update.poll)

async def receive_poll_answer(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Summarize a users poll vote"""
    answer = update.poll_answer
    print(answer)

if __name__ == '__main__':
    application = ApplicationBuilder().token(config.VariableConst.MY_TOKEN_BOT).build()

    application.add_handler(CommandHandler('start',start))
    application.add_handler(CommandHandler('poll', poll))
    application.add_handler(CommandHandler('quiz', quiz))

    application.add_handler(PollHandler(receive_quiz_answer))
    application.add_handler(PollAnswerHandler(receive_poll_answer))
    
    application.run_polling()